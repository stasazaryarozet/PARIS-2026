# Данные Telegram Bot группы "N, O, S"

Эта папка должна содержать символическую ссылку на данные группы "N, O, S" из Telegram Bot.

## Настройка

Запустите скрипт синхронизации:
```bash
./tools/sync_telegram_data.sh
```

Или создайте символическую ссылку вручную:
```bash
ln -s ~/Дела/Telegram\ Bot/data/chats/N_O_S ./source_materials/telegram_N_O_S
# Или
ln -s ~/TelegramArchive/{chat_id}_N_O_S ./source_materials/telegram_N_O_S
```

## Использование

Доступ к данным через Python утилиту:
```bash
python3 tools/get_telegram_data.py              # Статистика
python3 tools/get_telegram_data.py messages     # Список сообщений
python3 tools/get_telegram_data.py voice        # Голосовые файлы
python3 tools/get_telegram_data.py photos       # Фотографии
python3 tools/get_telegram_data.py search "текст"  # Поиск
```

## Участники группы

- **N** - Наталья Логинова (куратор)
- **O** - Ольга Розет (куратор)
- **S** - Стас Азарий Розет (организатор)
