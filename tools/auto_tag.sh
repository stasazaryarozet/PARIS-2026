#!/bin/bash
# Автоматическое создание семантических тегов после merge в main
# Использование: bash tools/auto_tag.sh
# Или через post-merge hook (автоматически)

set -e  # Exit on error

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Проверяем, что мы в main
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${YELLOW}⚠${NC}  Автоматическое тегирование работает только в main"
    echo "   Текущая ветка: $CURRENT_BRANCH"
    exit 0
fi

# Проверяем, что это merge commit
if ! git log -1 --pretty=%P | grep -q " "; then
    echo -e "${YELLOW}⚠${NC}  Пропускаем: не merge commit"
    exit 0
fi

echo -e "${BLUE}🏷️${NC}  Автоматическое создание тега..."

# Получаем последний тег
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v2.0.0")
echo "   Последний тег: $LAST_TAG"

# Парсим версию
if [[ $LAST_TAG =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
    MAJOR="${BASH_REMATCH[1]}"
    MINOR="${BASH_REMATCH[2]}"
    PATCH="${BASH_REMATCH[3]}"
else
    echo -e "${RED}✗${NC} Не могу распарсить тег: $LAST_TAG"
    echo "   Ожидается формат: v2.0.0"
    exit 1
fi

# Проверяем типы коммитов в merge для определения типа версии
MERGE_MESSAGE=$(git log -1 --pretty=%B)
COMMITS_IN_MERGE=$(git log --oneline origin/main..HEAD)

# Определяем тип инкремента
INCREMENT_TYPE="PATCH"  # По умолчанию patch

if echo "$COMMITS_IN_MERGE" | grep -qi "BREAKING CHANGE\|^feat!"; then
    INCREMENT_TYPE="MAJOR"
elif echo "$COMMITS_IN_MERGE" | grep -qi "^feat"; then
    INCREMENT_TYPE="MINOR"
fi

# Инкрементируем версию
case $INCREMENT_TYPE in
    MAJOR)
        MAJOR=$((MAJOR + 1))
        MINOR=0
        PATCH=0
        ;;
    MINOR)
        MINOR=$((MINOR + 1))
        PATCH=0
        ;;
    PATCH)
        PATCH=$((PATCH + 1))
        ;;
esac

NEW_TAG="v${MAJOR}.${MINOR}.${PATCH}"

# Извлекаем codename из WEBSITE_CONTENT.md (если есть)
CODENAME=""
if [ -f "WEBSITE_CONTENT.md" ]; then
    CODENAME=$(grep '^version:' WEBSITE_CONTENT.md | sed 's/version: "\(.*\)"/\1/' || echo "")
fi

# Формируем описание тега из коммитов в merge
TAG_MESSAGE="Release $NEW_TAG"
if [ -n "$CODENAME" ]; then
    TAG_MESSAGE="$TAG_MESSAGE: $CODENAME"
fi

echo ""
echo -e "${GREEN}✓${NC} Создание тега: $NEW_TAG"
echo "   Тип инкремента: $INCREMENT_TYPE"
if [ -n "$CODENAME" ]; then
    echo "   Codename: $CODENAME"
fi

# Создаем аннотированный тег
git tag -a "$NEW_TAG" -m "$TAG_MESSAGE" -m "" -m "Changes in this release:" -m "$COMMITS_IN_MERGE"

echo ""
echo -e "${GREEN}✓${NC} Тег создан локально: $NEW_TAG"
echo ""
echo "   Для публикации тега выполните:"
echo -e "   ${BLUE}git push origin $NEW_TAG${NC}"
echo ""

# Опционально: автоматический push тега
if [ "$AUTO_PUSH_TAG" = "1" ]; then
    echo -e "${BLUE}→${NC} Автоматический push тега..."
    git push origin "$NEW_TAG"
    echo -e "${GREEN}✓${NC} Тег опубликован: $NEW_TAG"
fi

exit 0

