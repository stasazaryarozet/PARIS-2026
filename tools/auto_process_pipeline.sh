#!/bin/bash
# Полностью автоматический pipeline: Telegram → Whisper → GPT-4 → PROJECT_KNOWLEDGE

set -e

PROJECT_DIR="/Users/azaryarozet/Library/Mobile Documents/com~apple~CloudDocs/Projects/paris-2026"
cd "$PROJECT_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🤖 АГЕНТСКИЙ PIPELINE: АВТОМАТИЧЕСКАЯ ОБРАБОТКА КОНТЕНТА"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ШАГ 1: Whisper транскрипция
echo "📹 ШАГ 1: Транскрипция видео через Whisper"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
python3 tools/process_telegram_videos.py

if [ $? -ne 0 ]; then
    echo "❌ Ошибка транскрипции"
    exit 1
fi

echo ""
echo "✅ Транскрипция завершена"
echo ""

# ШАГ 2: Проверить наличие транскриптов
TRANSCRIPT_COUNT=$(ls -1 "source_materials/telegram/transcripts/"*.txt 2>/dev/null | wc -l | tr -d ' ')

if [ "$TRANSCRIPT_COUNT" -eq 0 ]; then
    echo "⚠️  Транскрипты не найдены. Завершаю."
    exit 0
fi

echo "📄 Найдено транскриптов: $TRANSCRIPT_COUNT"
echo ""

# ШАГ 3: GPT-4 обработка (если API ключ установлен)
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY не установлен"
    echo "   Пропускаю GPT-4 обработку"
    echo ""
    echo "📝 Для автоматической обработки через GPT-4:"
    echo "   export OPENAI_API_KEY='sk-...'"
    echo ""
    exit 0
fi

echo "🤖 ШАГ 2: Извлечение данных через GPT-4"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
python3 tools/gpt_content_processor.py

if [ $? -ne 0 ]; then
    echo "❌ Ошибка GPT-4 обработки"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ PIPELINE ЗАВЕРШЕН"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 РЕЗУЛЬТАТЫ:"
echo "   Транскрипты: source_materials/telegram/transcripts/"
echo "   Извлеченные данные: source_materials/telegram/extracted/"
echo "   Обновлено: PROJECT_KNOWLEDGE.md"
echo ""




