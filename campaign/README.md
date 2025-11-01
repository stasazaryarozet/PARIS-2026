# CAMPAIGN / Кампания продвижения

Вся кампания продвижения тура PARIS-2026.

## Структура

```
campaign/
├── instagram/          # Instagram контент
│   ├── published/     # Опубликованные материалы
│   ├── drafts/        # Черновики и концепции
│   └── autogen/       # Автогенерация
├── landing/           # parisinjanuary.ru
│   ├── src/          # Исходники (HTML, CSS, JS, build.py)
│   ├── public/       # Статические ресурсы
│   ├── tests/        # Тесты
│   ├── hooks/        # Git hooks
│   └── docs/         # Документация
└── strategy/          # Стратегия кампании
    ├── prompts/      # AI промпты
    └── history/      # История разработки
```

## Instagram

### Published
Опубликованные посты и Stories с метриками:
- `2025-10-28_stories/` — триптих (s1, s2, s3)
- `2025-10-28_post.txt` — текст основного поста
- `metrics/` — IG Insights

### Drafts
Черновики текстов и изображений для будущих публикаций.

### Autogen
Автоматически генерируемые варианты Stories (instagram_stories/).

## Landing (parisinjanuary.ru)

### Деплой
- **Продакшн:** https://parisinjanuary.ru
- **Технологии:** GitHub Pages, HTML/CSS/JS, Python (build.py)
- **Автодеплой:** Push в `main` → GitHub Actions → деплой

### Разработка
```bash
# Генерация content.js из WEBSITE_CONTENT.md
cd landing/src
python3 build.py

# Запуск локального сервера
cd landing/server
python3 run.py

# Тесты
cd landing/tests
python3 test_build.py
```

### Источник правды
`landing/src/content/WEBSITE_CONTENT.md` — единый источник всего контента лендинга.

### Git Hooks
`landing/hooks/pre-commit.sh` — автоматическая валидация перед commit.

## Strategy

Стратегия кампании, концепции, промпты для AI-генерации:
- `CAMPAIGN_STRATEGY.md` — основная стратегия
- `prompts/` — промпты для Gemini, Mirror и других инструментов
- `history/` — история разработки и коммуникации

---

**Родительский проект:** [PARIS-2026](../README.md)

