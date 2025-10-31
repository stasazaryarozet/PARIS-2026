#!/usr/bin/env python3
"""
GPT-4 агентская обработка контента из Telegram
Извлекает структурированную информацию из транскриптов
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

try:
    from openai import OpenAI
except ImportError:
    print("❌ OpenAI SDK не установлен")
    print("   Запустите: pip3 install openai")
    sys.exit(1)

# API Key из переменной окружения
API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    print("❌ OPENAI_API_KEY не установлен")
    print("   Экспортируйте: export OPENAI_API_KEY='sk-...'")
    sys.exit(1)

client = OpenAI(api_key=API_KEY)

# Директории
TRANSCRIPT_DIR = Path('source_materials/telegram/transcripts')
METADATA_DIR = Path('source_materials/telegram/metadata')
EXTRACTED_DIR = Path('source_materials/telegram/extracted')
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)

# Системный промпт для GPT-4
SYSTEM_PROMPT = """Ты — агент для извлечения структурированной информации из транскриптов о кураторском туре "Париж 2026".

**КОНТЕКСТ ПРОЕКТА:**
- Премиальный 4-дневный тур в Париже (15-18 января 2026)
- Тема: Индивидуальный почерк ар-деко (100 лет с Exposition 1925)
- Кураторы: Ольга Розет (30+ лет в дизайне) и Наталья Логинова (резидент Парижа)
- Группа: до 12 человек
- Цена: 1550 €

**ПРОГРАММА:**
- День I (15.01): Правый берег — Printemps, Nolinski (Deniot), Legré, музей MAD
- День II (16.01): Левый берег — Saint-Germain, Galerie Vallois (Эйлин Грей), Expo 1937
- День III (17.01): Maison & Objet — What's New, Craft, Signature
- День IV (18.01): Maison Louis Carré (Aalto) — эргономика, материалы

**ТВОЯ ЗАДАЧА:**
Извлечь из транскрипта:

1. **Маршруты и локации:**
   - Названия мест (музеи, галереи, отели, магазины)
   - Адреса (если упомянуты)
   - Специфические детали (архитекторы, даты, материалы)
   - Время посещения
   - Последовательность

2. **Программные элементы:**
   - Изменения/дополнения к программе
   - Новые локации
   - Отмененные элементы
   - Альтернативы

3. **Экспертные инсайты:**
   - Цитаты о мастерах (Deniot, Эйлин Грей, Aalto, Rouhlmann)
   - Философия дизайна (материалы, фактуры, почерк)
   - Технические детали (техники, процессы)

4. **Организационные детали:**
   - Логистика (транспорт, время, встречи)
   - Контакты (владельцы галерей, кураторы)
   - Бронирования/предзаказы

5. **Визуальные референсы:**
   - Описания интерьеров
   - Специфические предметы/объекты
   - Цветовые палитры
   - Материалы (малабарское дерево, лак, стеклянные кирпичи)

**ФОРМАТ ВЫВОДА:**
JSON со структурой:
```json
{
  "summary": "Краткое резюме (2-3 предложения)",
  "locations": [
    {
      "name": "Название",
      "address": "Адрес (если есть)",
      "day": "День I/II/III/IV или null",
      "details": "Детали",
      "significance": "Почему важно"
    }
  ],
  "program_updates": [
    {
      "type": "addition/change/removal",
      "description": "Что изменилось"
    }
  ],
  "expert_insights": [
    {
      "topic": "Тема",
      "quote": "Прямая цитата (если есть)",
      "insight": "Инсайт"
    }
  ],
  "logistics": [
    {
      "item": "Элемент",
      "details": "Детали"
    }
  ],
  "visual_references": [
    {
      "description": "Описание",
      "context": "Контекст"
    }
  ],
  "action_items": [
    "Что нужно сделать (если упомянуто)"
  ]
}
```

**ПРИНЦИПЫ:**
- Точность: только факты из транскрипта
- Контекст: связывай с существующей программой
- Детальность: конкретные детали (имена, адреса, материалы)
- Приоритет: маршруты и локации > инсайты > логистика
- Язык: сохраняй русский язык, имена собственные — оригинальное написание

**ЕСЛИ ТРАНСКРИПТ НЕРАЗБОРЧИВ:**
Вернуть JSON с "error": "Описание проблемы"
"""


def process_transcript(transcript_path: Path):
    """Обрабатывает один транскрипт через GPT-4"""
    
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📄 Обрабатываю: {transcript_path.name}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Читаем транскрипт
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
    except Exception as e:
        print(f"❌ Ошибка чтения: {e}")
        return
    
    print(f"📊 Размер транскрипта: {len(transcript_text)} символов")
    print(f"🤖 Отправляю GPT-4...")
    
    start_time = datetime.now()
    
    try:
        # Вызываем GPT-4
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Транскрипт:\n\n{transcript_text}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.1,  # Низкая температура для точности
        )
        
        elapsed = (datetime.now() - start_time).total_seconds()
        
        # Извлекаем результат
        result = response.choices[0].message.content
        extracted_data = json.loads(result)
        
        # Сохраняем извлеченные данные
        output_name = transcript_path.stem + '_extracted.json'
        output_path = EXTRACTED_DIR / output_name
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Обработано за {elapsed:.1f} секунд")
        print(f"📁 Результат: {output_path.name}")
        
        # Показываем краткое резюме
        if 'summary' in extracted_data:
            print(f"\n📝 Резюме:")
            print(f"   {extracted_data['summary']}")
        
        if 'locations' in extracted_data:
            print(f"\n📍 Локаций найдено: {len(extracted_data['locations'])}")
            for loc in extracted_data['locations'][:3]:  # Первые 3
                print(f"   • {loc.get('name', 'N/A')}")
        
        if 'expert_insights' in extracted_data:
            print(f"\n💡 Инсайтов: {len(extracted_data['expert_insights'])}")
        
        print()
        
        return extracted_data
        
    except Exception as e:
        print(f"❌ Ошибка GPT-4: {e}")
        print()
        return None


def update_project_knowledge(extracted_data: dict, source_file: str):
    """Обновляет PROJECT_KNOWLEDGE.md с новой информацией"""
    
    knowledge_path = Path('PROJECT_KNOWLEDGE.md')
    
    # Создаем секцию для обновлений
    update_section = f"\n\n---\n\n## ОБНОВЛЕНИЕ ИЗ TELEGRAM ({datetime.now().strftime('%Y-%m-%d')})\n\n"
    update_section += f"**Источник:** `{source_file}`\n\n"
    
    # Добавляем локации
    if extracted_data.get('locations'):
        update_section += "### Новые/Уточненные Локации\n\n"
        for loc in extracted_data['locations']:
            update_section += f"**{loc.get('name', 'N/A')}**\n"
            if loc.get('address'):
                update_section += f"- Адрес: {loc['address']}\n"
            if loc.get('day'):
                update_section += f"- День: {loc['day']}\n"
            if loc.get('details'):
                update_section += f"- Детали: {loc['details']}\n"
            if loc.get('significance'):
                update_section += f"- Значение: {loc['significance']}\n"
            update_section += "\n"
    
    # Добавляем инсайты
    if extracted_data.get('expert_insights'):
        update_section += "### Экспертные Инсайты\n\n"
        for insight in extracted_data['expert_insights']:
            update_section += f"**{insight.get('topic', 'N/A')}**\n"
            if insight.get('quote'):
                update_section += f"> \"{insight['quote']}\"\n\n"
            if insight.get('insight'):
                update_section += f"{insight['insight']}\n\n"
    
    # Добавляем в конец файла
    try:
        with open(knowledge_path, 'a', encoding='utf-8') as f:
            f.write(update_section)
        print(f"✅ PROJECT_KNOWLEDGE.md обновлен")
    except Exception as e:
        print(f"❌ Ошибка обновления PROJECT_KNOWLEDGE.md: {e}")


def main():
    print("")
    print("🤖 GPT-4 АГЕНТСКАЯ ОБРАБОТКА КОНТЕНТА")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Модель: gpt-4-turbo-preview")
    print(f"Директория транскриптов: {TRANSCRIPT_DIR}")
    print(f"Директория результатов: {EXTRACTED_DIR}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    
    # Получаем список транскриптов
    transcripts = sorted(TRANSCRIPT_DIR.glob('*.txt'))
    
    if not transcripts:
        print("❌ Транскрипты не найдены")
        print(f"   Ожидаемая директория: {TRANSCRIPT_DIR}")
        sys.exit(1)
    
    print(f"📄 Найдено транскриптов: {len(transcripts)}")
    print()
    
    # Обрабатываем каждый транскрипт
    all_extracted = []
    
    for i, transcript_path in enumerate(transcripts, 1):
        print(f"[{i}/{len(transcripts)}]")
        
        # Проверяем, не обработан ли уже
        output_name = transcript_path.stem + '_extracted.json'
        output_path = EXTRACTED_DIR / output_name
        
        if output_path.exists():
            print(f"⏩ Пропускаю {transcript_path.name} (уже обработан)")
            print()
            
            # Читаем существующий результат
            with open(output_path, 'r', encoding='utf-8') as f:
                all_extracted.append(json.load(f))
            
            continue
        
        # Обрабатываем
        extracted = process_transcript(transcript_path)
        
        if extracted:
            all_extracted.append(extracted)
            
            # Обновляем PROJECT_KNOWLEDGE.md
            update_project_knowledge(extracted, transcript_path.name)
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✅ ВСЕ ТРАНСКРИПТЫ ОБРАБОТАНЫ")
    print(f"📁 Результаты: {EXTRACTED_DIR}")
    print(f"📝 PROJECT_KNOWLEDGE.md обновлен")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


if __name__ == '__main__':
    main()




