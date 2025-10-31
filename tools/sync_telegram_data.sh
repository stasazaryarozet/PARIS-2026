#!/bin/bash
# Скрипт синхронизации данных Telegram Bot группы "N, O, S" в проект PARIS 2026

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$PROJECT_ROOT/source_materials/telegram_N_O_S"

# Пути к источникам данных (проверяются в порядке приоритета)
SOURCES=(
    "$HOME/Дела/Telegram Bot/data/chats/N_O_S"
    "$HOME/TelegramArchive/"*"_N_O_S"
    "$HOME/TelegramArchive/"*"N_O_S"*
)

echo "🔍 Поиск данных группы N, O, S..."

SOURCE=""
for src in "${SOURCES[@]}"; do
    if [ -d "$src" ]; then
        SOURCE="$src"
        echo "✅ Найден источник: $SOURCE"
        break
    fi
done

if [ -z "$SOURCE" ]; then
    echo "⚠️  Источник данных не найден. Проверьте пути:"
    for src in "${SOURCES[@]}"; do
        echo "   - $src"
    done
    echo ""
    echo "Создаю символическую ссылку вручную:"
    echo "  ln -s <путь_к_данным> $TARGET_DIR"
    exit 1
fi

# Создаем целевую директорию
mkdir -p "$(dirname "$TARGET_DIR")"

# Если уже есть символическая ссылка, проверяем корректность
if [ -L "$TARGET_DIR" ]; then
    CURRENT_TARGET=$(readlink -f "$TARGET_DIR")
    if [ "$CURRENT_TARGET" != "$(readlink -f "$SOURCE")" ]; then
        echo "🔄 Обновление символической ссылки..."
        rm "$TARGET_DIR"
        ln -s "$SOURCE" "$TARGET_DIR"
    else
        echo "✅ Символическая ссылка уже настроена корректно"
    fi
elif [ -d "$TARGET_DIR" ] && [ ! -L "$TARGET_DIR" ]; then
    echo "⚠️  $TARGET_DIR существует как директория, не ссылка"
    echo "   Создаю символическую ссылку..."
    mv "$TARGET_DIR" "${TARGET_DIR}.backup"
    ln -s "$SOURCE" "$TARGET_DIR"
elif [ ! -e "$TARGET_DIR" ]; then
    echo "🔗 Создание символической ссылки: $TARGET_DIR -> $SOURCE"
    ln -s "$SOURCE" "$TARGET_DIR"
fi

echo "✅ Интеграция настроена успешно!"
echo "   Данные доступны в: $TARGET_DIR"
