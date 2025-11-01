# После Перезагрузки — Обработка Видео от Натальи

**Дата**: 29 октября 2025  
**Статус**: Видео получено (54MB, 18:16)

---

## ЧТО УЖЕ СДЕЛАНО

✅ Telegram Bot настроен и работает  
✅ Видео от Натальи получено:
```
source_materials/telegram/videos/natalia_manual_20251029_182058.mp4
```
✅ Whisper установлен

---

## СЛЕДУЮЩИЙ ШАГ: ТРАНСКРИПЦИЯ

### Почему Whisper "зависает"

Whisper = нейросеть для расшифровки речи (OpenAI).

**Технически**:
- Загружает модель (1.5GB для medium)
- Обрабатывает аудио по сегментам (30 секунд)
- Для 18-минутного видео = 36 сегментов
- Время: **5-10 минут** на MacBook M1/M2

**Это нормально**. Не зависание, а длительная обработка.

---

## ОПТИМАЛЬНОЕ РЕШЕНИЕ

### Вариант A: Фоновый скрипт (рекомендую)

```bash
cd "/Users/azaryarozet/Library/Mobile Documents/com~apple~CloudDocs/Projects/paris-2026"

# Запуск в фоне
nohup python3 tools/process_telegram_videos.py > logs/whisper.log 2>&1 &

# PID сохранится
echo $! > logs/whisper.pid

# Следить за прогрессом
tail -f logs/whisper.log
```

Скрипт `tools/process_telegram_videos.py` создан и:
- Обрабатывает все видео последовательно
- Логирует прогресс
- Сохраняет транскрипты в `source_materials/telegram/transcripts/`
- Работает в фоне

### Вариант B: Ручная команда (если скрипт не нужен)

```bash
cd "/Users/azaryarozet/Library/Mobile Documents/com~apple~CloudDocs/Projects/paris-2026"

python3 -m whisper \
  "source_materials/telegram/videos/natalia_manual_20251029_182058.mp4" \
  --model base \
  --language Russian \
  --output_format txt \
  --output_dir "source_materials/telegram/transcripts" \
  --fp16 False
```

**Параметры**:
- `--model base` — легкая модель (быстрее, но менее точная)
- `--fp16 False` — совместимость с CPU (если нет GPU)

**Время**: ~5 минут для 18-минутного видео.

### Вариант C: Онлайн-сервис (если локально медленно)

1. https://www.happyscribe.com/ru — автоматическая транскрипция
2. Загрузить видео
3. Скачать транскрипт (.txt)
4. Сохранить в `source_materials/telegram/transcripts/`

---

## ПОСЛЕ ТРАНСКРИПЦИИ

Скажите Claude:
```
"Обработай транскрипт от Натальи"
```

Claude автоматически:
1. Читает транскрипт
2. Извлекает факты (адреса, имена, даты)
3. Обновляет `PROJECT_KNOWLEDGE.md`:
   - Маршруты
   - Программа
   - Детали о галереях/музеях
4. Обновляет `WEBSITE_CONTENT.md` (если нужны правки)

---

## КОНТЕКСТ: ПОЧЕМУ ДОЛГО

### Whisper Architecture

OpenAI Whisper (2022):
> "Whisper is a general-purpose speech recognition model trained on 680,000 hours of multilingual data."

Источник: https://github.com/openai/whisper

**Модели** (размер → качество → скорость):

| Модель | Параметры | Время (18 мин видео) | Качество |
|---|---|---|---|
| tiny | 39M | ~1 мин | Низкое |
| base | 74M | ~3 мин | Среднее |
| small | 244M | ~5 мин | Хорошее |
| medium | 769M | ~10 мин | Отличное |
| large | 1550M | ~20 мин | Максимум |

**Рекомендация**: `base` для первой попытки (быстро, достаточно точно).

### Почему не real-time

Whisper использует Transformer архитектуру:
> "The model processes audio in 30-second segments with overlapping windows."

Каждый сегмент:
1. Конвертация аудио → mel-spectrogram
2. Encoder: audio features → 1280-dim vectors
3. Decoder: vectors → text tokens
4. Post-processing: timestamps, punctuation

Для 18-минутного видео:
- 36 сегментов × 10-20 секунд на сегмент = 6-12 минут

**CPU vs GPU**:
- MacBook M1/M2 (Neural Engine): ~10 минут
- Intel CPU: ~20-30 минут
- NVIDIA GPU: ~3-5 минут

---

## ЕСЛИ WHISPER СЛИШКОМ МЕДЛЕННО

### Альтернатива: Faster-Whisper

Optimized C++ implementation:

```bash
pip3 install faster-whisper

python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('base', device='cpu')
segments, _ = model.transcribe('source_materials/telegram/videos/natalia_manual_20251029_182058.mp4')
with open('source_materials/telegram/transcripts/natalia_transcript.txt', 'w') as f:
    for segment in segments:
        f.write(segment.text + '\n')
"
```

**Скорость**: 2-3× быстрее чем оригинальный Whisper.

---

## ПОСЛЕ ПЕРЕЗАГРУЗКИ

1. Откройте `AFTER_RESTART_VIDEO_PROCESSING.md` (этот файл)
2. Выберите Вариант A, B или C
3. Дождитесь завершения транскрипции
4. Скажите Claude: **"Обработай транскрипт"**

---

**Статус**: Whisper установлен, видео готово к обработке.





