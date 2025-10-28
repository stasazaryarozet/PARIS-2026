#!/usr/bin/env bash
set -euo pipefail

# release.sh — автоматизация протокола деплоя (подтверждена Claude)
# Шаги: bump версии → build → commit → push
# Версии поддерживают кодовые имена: v<число>-<кодовое_имя>, где кодовое имя — одно слово латиницей

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 не найден" >&2; exit 1
fi

# 1) Bump версии в WEBSITE_CONTENT.md (обязателен)
if [[ $# -lt 1 ]]; then
  echo "Usage: tools/release.sh v<NN>-<codename> 'Описание'" >&2
  exit 1
fi

VERSION="$1"  # например: v125-aurora
MESSAGE="${2:-release}"

if ! grep -q '^version: "' WEBSITE_CONTENT.md; then
  echo "Не найден frontmatter 'version' в WEBSITE_CONTENT.md" >&2; exit 1
fi

# Извлекаем кодовое имя для frontmatter (после дефиса) и полную версию — для коммита
CODENAME=$(echo "$VERSION" | sed -E 's/^v[0-9]+-//')
sed -E -i '' "s/^version: \"[^\"]+\"/version: \"${CODENAME}\"/" WEBSITE_CONTENT.md

# 2) Регенерация content.js
python3 build.py

# 3) Commit + push
git add -A
git commit -m "${VERSION}: ${MESSAGE}"
git push

echo "✓ Released ${VERSION}"

