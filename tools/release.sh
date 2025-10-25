#!/usr/bin/env bash
set -euo pipefail

# release.sh — автоматизация протокола деплоя (подтверждена Claude)
# Шаги: bump версии → build → commit → push

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 не найден" >&2; exit 1
fi

# 1) Bump версии в WEBSITE_CONTENT.md (обязателен)
if [[ $# -lt 1 ]]; then
  echo "Usage: tools/release.sh vXYZ 'Описание'" >&2
  exit 1
fi

VERSION="$1"
MESSAGE="${2:-release}"

if ! grep -q '^version: "' WEBSITE_CONTENT.md; then
  echo "Не найден frontmatter 'version' в WEBSITE_CONTENT.md" >&2; exit 1
fi

sed -E -i '' "s/^version: \"[0-9]+\"/version: \"${VERSION#v}\"/" WEBSITE_CONTENT.md

# 2) Регенерация content.js
python3 build.py

# 3) Commit + push
git add -A
git commit -m "${VERSION}: ${MESSAGE}"
git push

echo "✓ Released ${VERSION}"

