# paris-2026

Премиальный кураторский тур по ар-деко Парижу.

## 📋 Оглавление

- [О проекте](#о-проекте)
- [Быстрый старт](#быстрый-старт)
- [Git Workflow](#git-workflow)
- [Структура проекта](#структура-проекта)
- [Разработка](#разработка)
- [Документация](#документация)

---

## О проекте

Одностраничный сайт для продвижения 4-дневного кураторского тура по Парижу с фокусом на ар-деко архитектуру и дизайн (январь 2026).

**Технологии**: Pure HTML/CSS/JavaScript (без фреймворков)

**Особенности**:
- Билингвальность (RU/AR с RTL поддержкой)
- Премиальный минималистичный дизайн
- Responsive для всех устройств
- Форма бронирования с валидацией

---

## Быстрый старт

### Клонирование

```bash
git clone https://github.com/stasazaryarozet/paris-2026.git
cd paris-2026
```

### Просмотр сайта

```bash
# Открыть index.html в браузере
open index.html

# Или запустить локальный сервер
python3 -m http.server 8000
# Открыть http://localhost:8000
```

### Первоначальная настройка Git

```bash
# Настроить commit template
git config commit.template .gitmessage

# Настроить автора
git config user.name "Ваше Имя"
git config user.email "your@email.com"

# Добавить алиасы
git config alias.st status
git config alias.co checkout
git config alias.br branch
git config alias.ci commit
git config alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

---

## Git Workflow

Проект использует **structured Git workflow** с branch protection и automated hooks.

### Основные ветки

- `main` - Production-ready код (защищена)
- `develop` - Integration branch для разработки
- `feature/*` - Новая функциональность
- `fix/*` - Исправления багов
- `hotfix/*` - Критические исправления для production

### Commit Convention

Проект следует [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>
```

**Типы**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

**Примеры**:
```bash
feat(form): добавить валидацию email
fix(i18n): исправить RTL направление для арабского
docs: обновить README
style(design): увеличить размер заголовков
```

### Типовой workflow

```bash
# 1. Создать feature ветку
git checkout develop
git pull
git checkout -b feature/my-feature

# 2. Разработка и коммиты
git add .
git commit  # используйте commit template

# 3. Push и Pull Request
git push -u origin feature/my-feature
# Создать PR: feature/my-feature → develop

# 4. После merge - cleanup
git checkout develop
git pull
git branch -d feature/my-feature
```

📚 **Подробнее**: [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) | [GIT_QUICKSTART.md](./GIT_QUICKSTART.md)

---

## Структура проекта

```
paris-2026/
├── index.html              # Главная страница (единственная)
├── og-image.jpg            # Open Graph изображение
├── README.md               # Этот файл
├── GIT_WORKFLOW.md         # Полная документация по Git
├── GIT_QUICKSTART.md       # Быстрый справочник по Git
├── PROJECT_KNOWLEDGE_GRAPH.json  # Knowledge base для AI
│
├── .git/
│   └── hooks/              # Git hooks (автоматические проверки)
│       ├── pre-commit      # Проверки перед коммитом
│       ├── commit-msg      # Валидация commit message
│       └── pre-push        # Проверки перед push
│
├── .gitattributes          # Git файл атрибуты
├── .gitignore              # Игнорируемые файлы
├── .gitmessage             # Template для commit messages
│
└── source_materials/       # Исходные материалы
```

---

## Разработка

### Локальная разработка

1. Внести изменения в `index.html` или другие файлы
2. Открыть `index.html` в браузере для проверки
3. Закоммитить изменения:

```bash
git add .
git commit  # откроется редактор с template
```

### Pre-commit checks

Перед каждым коммитом автоматически выполняется:
- Проверка синтаксиса (Python, JS)
- Проверка размера файлов
- Проверка на forbidden patterns
- Предупреждения о коммитах в protected ветки

### Commit message validation

При коммите валидируется формат сообщения:
- Соответствие Conventional Commits
- Длина subject (макс 72 символа)
- Отсутствие точки в конце subject
- Отсутствие запрещенных слов (WIP, TODO и т.д.)

### Деплой

Проект деплоится автоматически на **GitHub Pages** при push в `main`.

**URL**: https://parisinjanuary.ru (или GitHub Pages URL)

---

## Документация

### Git

- [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) - Полная архитектура Git workflow
- [GIT_QUICKSTART.md](./GIT_QUICKSTART.md) - Быстрый справочник команд
- [.gitmessage](./.gitmessage) - Шаблон commit message

### Проект

- [PROJECT_KNOWLEDGE_GRAPH.json](./PROJECT_KNOWLEDGE_GRAPH.json) - Структурированная база знаний

### Конфигурация

- [.gitattributes](./.gitattributes) - Настройки обработки файлов в Git
- [.gitignore](./.gitignore) - Игнорируемые файлы и директории

---

## Команды на каждый день

```bash
# Статус
git st

# Красивый лог
git lg

# Создать feature ветку
git checkout develop && git pull && git checkout -b feature/new-thing

# Коммит
git add .
git commit  # используйте template

# Push
git push -u origin feature/new-thing

# Синхронизация develop
git checkout develop
git pull

# Обновить feature ветку
git checkout feature/my-feature
git rebase develop
```

---

## Troubleshooting

### Git hooks не работают

```bash
# Сделать hooks исполняемыми
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/commit-msg
chmod +x .git/hooks/pre-push
```

### Commit template не применяется

```bash
# Настроить template
git config commit.template .gitmessage

# Проверить
git config --get commit.template
```

### Merge конфликты

```bash
# Отменить merge
git merge --abort

# Отменить rebase
git rebase --abort
```

---

## Contributing

1. Создать feature ветку из `develop`
2. Следовать commit conventions
3. Создать Pull Request в `develop`
4. Дождаться code review
5. После merge - удалить feature ветку

---

## License

Proprietary - All rights reserved

---

## Контакты

**Проект**: paris-2026  
**Репозиторий**: https://github.com/stasazaryarozet/paris-2026  
**Сайт**: https://parisinjanuary.ru

---

**Создано**: 2024  
**Обновлено**: 2025-10-26
