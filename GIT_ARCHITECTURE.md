# Git Architecture - Полная архитектура проекта
## Paris-2026 Repository Structure

**Версия**: 2.0  
**Дата**: 2025-10-26  
**Статус**: Production

---

## 📋 Оглавление

1. [Обзор](#обзор)
2. [Философия](#философия)
3. [Структура репозитория](#структура-репозитория)
4. [Branching Model](#branching-model)
5. [Commit Conventions](#commit-conventions)
6. [Hooks System](#hooks-system)
7. [GitHub Integration](#github-integration)
8. [Workflow Scenarios](#workflow-scenarios)
9. [Защита и безопасность](#защита-и-безопасность)
10. [Автоматизация](#автоматизация)
11. [Troubleshooting](#troubleshooting)

---

## Обзор

Эта архитектура создана для обеспечения:
- ✅ **Чистоты истории**: Каждый коммит рассказывает историю
- ✅ **Безопасности**: Защита от случайных ошибок
- ✅ **Автоматизации**: Минимум ручной работы
- ✅ **Масштабируемости**: Легко добавлять новые процессы
- ✅ **Прозрачности**: Понятные процессы для всех

---

## Философия

### Принципы

1. **Single Source of Truth**
   - `main` - единственный production-ready код
   - История коммитов - источник правды о развитии
   - Теги - точки стабильных релизов

2. **Атомарность**
   - Один коммит = одно логическое изменение
   - Легко найти, понять, откатить

3. **Автоматизация превыше всего**
   - Hooks делают рутинную работу
   - CI/CD проверяет качество
   - Меньше человеческих ошибок

4. **Защита критического**
   - Protected branches
   - Обязательные проверки
   - PR-based workflow для production

---

## Структура репозитория

### Основные ветки

```
main (production)
  ↑
  └── develop (integration)
        ↑
        ├── feature/* (новые фичи)
        ├── fix/* (исправления)
        ├── hotfix/* (критические фиксы для main)
        ├── docs/* (документация)
        └── experiment/* (эксперименты)
```

### Детальное описание веток

#### `main` - Production Branch
- **Защита**: ✅ Protected, no direct commits
- **Слияние**: Только через PR из develop или hotfix/*
- **Деплой**: Автоматический на GitHub Pages
- **Правило**: Каждый merge commit = новый тег
- **Использование**: Только стабильный, протестированный код

#### `develop` - Integration Branch
- **Защита**: ⚠️ No force push
- **Слияние**: Из feature/*, fix/*, docs/*
- **Правило**: Код должен быть готов к релизу
- **Использование**: Интеграция всех изменений перед релизом

#### `feature/*` - Feature Branches
- **Формат**: `feature/<short-description>`
- **Примеры**: 
  - `feature/arabic-language`
  - `feature/booking-form`
  - `feature/gallery`
- **Создается из**: develop
- **Мерджится в**: develop
- **Жизненный цикл**: 
  1. Создать из develop
  2. Разработка
  3. PR → develop
  4. Code review
  5. Merge + Delete

#### `fix/*` - Bug Fix Branches
- **Формат**: `fix/<short-description>`
- **Примеры**:
  - `fix/mobile-menu-overlap`
  - `fix/rtl-direction`
- **Создается из**: develop
- **Мерджится в**: develop
- **Приоритет**: Средний

#### `hotfix/*` - Critical Fixes
- **Формат**: `hotfix/v<version>-<description>`
- **Примеры**:
  - `hotfix/v1.2.1-form-submission`
  - `hotfix/v1.1.5-payment-bug`
- **Создается из**: main
- **Мерджится в**: main И develop (важно!)
- **Использование**: ТОЛЬКО критические баги в production
- **Приоритет**: Максимальный

#### `docs/*` - Documentation
- **Формат**: `docs/<what-to-document>`
- **Примеры**:
  - `docs/api-documentation`
  - `docs/setup-guide`
- **Создается из**: develop
- **Мерджится в**: develop

#### `experiment/*` - Experiments
- **Формат**: `experiment/<what-testing>`
- **Примеры**:
  - `experiment/parallax-effect`
  - `experiment/animations`
- **Правило**: Может быть удалена без merge
- **Использование**: Тестирование идей

---

## Branching Model

### Git Flow Adaptation

```
┌─────────────────────────────────────────┐
│              main (v1.0)                │ ← Production
└──────────────┬──────────────────────────┘
               │ merge (tag v1.0)
               ↑
┌──────────────┴──────────────────────────┐
│            develop                      │ ← Integration
└──┬───────┬───────┬───────┬──────────────┘
   │       │       │       │
   ↓       ↓       ↓       ↓
feature/  fix/  docs/  experiment/
```

### Workflow Rules

1. **Никогда не коммитить напрямую в main**
2. **develop - основная рабочая ветка**
3. **feature/* для новых фич**
4. **hotfix/* только для критических багов в production**
5. **Удалять merged ветки**

---

## Commit Conventions

### Формат

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Описание | Когда использовать |
|------|----------|-------------------|
| `feat` | Новая функциональность | Добавление новых возможностей |
| `fix` | Исправление бага | Фиксы ошибок |
| `docs` | Документация | Изменения в документации |
| `style` | Стили/форматирование | CSS, отступы, форматирование |
| `refactor` | Рефакторинг | Изменение кода без изменения функциональности |
| `perf` | Производительность | Оптимизации |
| `test` | Тесты | Добавление/изменение тестов |
| `build` | Build система | Изменения в build процессе |
| `ci` | CI/CD | Изменения в CI/CD пайплайне |
| `chore` | Рутина | Обновление зависимостей, конфигурации |
| `revert` | Откат | Откат предыдущего коммита |

### Scopes (области)

- `content` - текстовый контент
- `design` - визуальный дизайн
- `form` - форма бронирования
- `i18n` - интернационализация
- `build` - build система
- `deps` - зависимости
- `config` - конфигурация
- `docs` - документация
- `seo` - SEO оптимизация

### Примеры

✅ **Правильно:**
```
feat(form): добавить валидацию email

Добавлена клиентская валидация email адреса:
- Проверка формата
- Визуальная индикация ошибки
- Сообщение пользователю

Closes #123
```

```
fix(i18n): исправить RTL direction для арабского

Направление текста теперь корректно переключается
при смене языка на арабский.

Fixes #456
```

```
docs: обновить инструкции по деплою

Добавлены шаги для настройки GitHub Pages
```

❌ **Неправильно:**
```
Добавил форму                    # Нет типа и формата
fixed bug                        # Не информативно
WIP: форма валидации.            # WIP не должен коммититься
Обновление                       # Слишком общее
```

---

## Hooks System

### Установленные Hooks

#### 1. `pre-commit`
**Расположение**: `.git/hooks/pre-commit` → `../../pre-commit.sh`

**Выполняет**:
- ✅ Обнаружение изменений в критических файлах
- ✅ Автоматическая регенерация `content.js` при изменении `WEBSITE_CONTENT.md`
- ✅ Запуск тестов (`test_build.py`)
- ✅ Проверка синтаксиса

**Блокирует коммит если**:
- Тесты не проходят
- Build fails
- Синтаксические ошибки

#### 2. `commit-msg`
**Расположение**: `.git/hooks/commit-msg`

**Выполняет**:
- ✅ Валидация формата commit message
- ✅ Проверка типа коммита
- ✅ Проверка длины заголовка (<100 символов)
- ✅ Запрет точки в конце заголовка
- ✅ Запрет WIP/TODO в main/master

**Блокирует коммит если**:
- Неверный формат
- Запрещенные слова в production ветке
- Заголовок заканчивается точкой

#### 3. `prepare-commit-msg`
**Расположение**: `.git/hooks/prepare-commit-msg`

**Выполняет**:
- ✅ Автоматическое добавление template в commit message
- ✅ Определение scope из имени ветки
- ✅ Предзаполнение типа для feature/fix веток

**Примеры**:
- В `feature/booking-form` → `feat(booking-form): `
- В `fix/mobile-menu` → `fix(mobile-menu): `

#### 4. `pre-push`
**Расположение**: `.git/hooks/pre-push`

**Выполняет**:
- ✅ Защита от прямого push в main/master
- ✅ Полный запуск тестов
- ✅ Проверка build
- ✅ Предупреждение о force push
- ✅ Проверка наличия TODO/FIXME в коммитах

**Блокирует push если**:
- Push в protected branch без флага
- Тесты не проходят
- Build fails
- Force push в protected branch

#### 5. `post-commit`
**Расположение**: `.git/hooks/post-commit`

**Выполняет**:
- ℹ️ Информация о созданном коммите
- ℹ️ Напоминание о push для feature веток
- ℹ️ Подсказка о создании PR

**Не блокирует**: Только информационный hook

### Обход защиты (для emergency)

```bash
# Пропустить pre-commit hook
git commit --no-verify -m "message"

# Разрешить push в main (только для hotfix!)
ALLOW_MAIN_PUSH=1 git push origin main
```

⚠️ **Используйте редко и осознанно!**

---

## GitHub Integration

### Pull Request Template

**Расположение**: `.github/PULL_REQUEST_TEMPLATE.md`

**Содержит**:
- Описание изменений
- Тип изменений (bug/feature/etc)
- Тестирование
- Скриншоты
- Чеклист
- Breaking changes

### Issue Templates

#### Bug Report
**Расположение**: `.github/ISSUE_TEMPLATE/bug_report.md`

**Содержит**:
- Описание бага
- Шаги воспроизведения
- Ожидаемое/фактическое поведение
- Скриншоты
- Окружение
- Приоритет

#### Feature Request
**Расположение**: `.github/ISSUE_TEMPLATE/feature_request.md`

**Содержит**:
- Описание фичи
- Проблема которую решает
- Предлагаемое решение
- Mockups
- Приоритет
- Критерии приемки

### GitHub Actions

**Расположение**: `.github/workflows/deploy.yml`

**Pipeline**:
1. Trigger: Push to main
2. Build проект
3. Запуск тестов
4. Deploy на GitHub Pages

---

## Workflow Scenarios

### Сценарий 1: Новая фича

```bash
# 1. Убедиться что develop актуален
git checkout develop
git pull origin develop

# 2. Создать feature ветку
git checkout -b feature/booking-validation

# 3. Разработка с коммитами
git add src/form.js
git commit
# Откроется редактор с template: feat(booking-validation):

# 4. Продолжить разработку
git add src/validation.js
git commit -m "feat(form): добавить email валидацию"

git add test/validation.test.js
git commit -m "test(form): добавить тесты для валидации"

# 5. Push ветки
git push origin feature/booking-validation

# 6. Создать Pull Request на GitHub
# feature/booking-validation → develop

# 7. Code review → Approve → Merge

# 8. Удалить ветку
git branch -d feature/booking-validation
git push origin --delete feature/booking-validation
```

### Сценарий 2: Исправление бага

```bash
# 1. Создать fix ветку
git checkout develop
git pull origin develop
git checkout -b fix/mobile-menu-z-index

# 2. Исправление
git add style.css
git commit -m "fix(design): исправить z-index мобильного меню"

# 3. Push и PR
git push origin fix/mobile-menu-z-index
# Создать PR → develop

# 4. После merge удалить ветку
```

### Сценарий 3: Критический hotfix

```bash
# 1. Создать hotfix из main
git checkout main
git pull origin main
git checkout -b hotfix/v1.2.1-form-crash

# 2. Исправление
git add index.html
git commit -m "fix(form): исправить crash при отправке формы"

# 3. Тестирование
npm test

# 4. Merge в main
git checkout main
git merge --no-ff hotfix/v1.2.1-form-crash
git tag -a v1.2.1 -m "Hotfix: исправление краша формы"

# 5. Push в main
ALLOW_MAIN_PUSH=1 git push origin main --tags

# 6. Merge в develop (важно!)
git checkout develop
git merge --no-ff hotfix/v1.2.1-form-crash
git push origin develop

# 7. Удалить hotfix ветку
git branch -d hotfix/v1.2.1-form-crash
git push origin --delete hotfix/v1.2.1-form-crash
```

### Сценарий 4: Релиз (develop → main)

```bash
# 1. Убедиться что develop готов
git checkout develop
git pull origin develop

# Запустить все тесты
npm test

# 2. Создать release ветку (опционально)
git checkout -b release/v1.3.0

# 3. Финальные правки (версии, CHANGELOG)
# Обновить версию в WEBSITE_CONTENT.md
git add WEBSITE_CONTENT.md
git commit -m "chore(release): bump version to v1.3.0"

# 4. Merge в main через PR
# Создать PR: release/v1.3.0 → main

# 5. После merge создать тег
git checkout main
git pull origin main
git tag -a v1.3.0 -m "Release v1.3.0: Arabic localization"
git push origin main --tags

# 6. Merge обратно в develop
git checkout develop
git merge --no-ff main
git push origin develop
```

### Сценарий 5: Быстрые правки контента

```bash
# Для небольших правок можно работать с develop напрямую
git checkout develop
git pull origin develop

# Редактирование
git add WEBSITE_CONTENT.md
git commit -m "docs(content): обновить описание дня 3"

git push origin develop
```

---

## Защита и безопасность

### Protected Branches на GitHub

#### Main Branch
**Настройки** (Settings → Branches → Add rule):
```
Branch name pattern: main

☑ Require pull request reviews before merging
  └ Required approvals: 1
☑ Dismiss stale pull request approvals when new commits are pushed
☑ Require status checks to pass before merging
  └ Require branches to be up to date before merging
  └ Status checks: build, test
☑ Require conversation resolution before merging
☑ Require signed commits (опционально)
☑ Include administrators
☑ Allow force pushes: ❌ NO
☑ Allow deletions: ❌ NO
```

#### Develop Branch
**Настройки**:
```
Branch name pattern: develop

☑ Require status checks to pass before merging
☑ Allow force pushes: ❌ NO
☐ Require pull request reviews (опционально)
```

### Branch Protection Rules

| Ветка | Direct Commit | Force Push | Delete | PR Required |
|-------|---------------|------------|--------|-------------|
| main | ❌ | ❌ | ❌ | ✅ |
| develop | ⚠️ (minor) | ❌ | ❌ | ⚠️ (recommended) |
| feature/* | ✅ | ⚠️ (own only) | ✅ | - |
| fix/* | ✅ | ⚠️ (own only) | ✅ | - |
| hotfix/* | ✅ | ❌ | ✅ (after merge) | - |

---

## Автоматизация

### Git Aliases

Добавьте в `~/.gitconfig` или `.git/config`:

```ini
[alias]
    # Shortcuts
    co = checkout
    br = branch
    ci = commit
    st = status
    unstage = restore --staged
    
    # Pretty logs
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    
    # Branch management
    feat = "!f() { git checkout develop && git pull && git checkout -b feature/$1; }; f"
    fix = "!f() { git checkout develop && git pull && git checkout -b fix/$1; }; f"
    hot = "!f() { git checkout main && git pull && git checkout -b hotfix/$1; }; f"
    
    # Cleanup merged branches
    cleanup = "!git branch --merged | grep -v '\\*\\|main\\|develop' | xargs -n 1 git branch -d"
    
    # Quick amend
    amend = commit --amend --no-edit
    
    # Show my work today
    today = log --since='1 day ago' --oneline --author=\"$(git config user.name)\"
    
    # Undo last commit (keep changes)
    undo = reset --soft HEAD~1
```

### Использование:

```bash
# Быстро создать feature ветку
git feat booking-form
# Вместо: git checkout develop && git pull && git checkout -b feature/booking-form

# Создать fix ветку
git fix mobile-menu

# Создать hotfix ветку
git hot v1.2.1-crash

# Красивый лог
git lg

# Удалить merged ветки
git cleanup

# Быстро поправить последний коммит
git add forgotten-file.js
git amend
```

---

## Troubleshooting

### Проблема: Случайно закоммитил в main

```bash
# 1. Создать ветку с изменениями
git branch rescue/accidental-commit

# 2. Откатить main
git reset --hard HEAD~1

# 3. Переключиться на rescue ветку
git checkout rescue/accidental-commit

# 4. Создать правильную ветку и PR
git checkout develop
git checkout -b fix/proper-branch
git cherry-pick rescue/accidental-commit

# 5. Удалить rescue ветку
git branch -D rescue/accidental-commit
```

### Проблема: Нужно изменить последний commit message

```bash
# Если еще НЕ запушил
git commit --amend -m "Новое правильное сообщение"

# Если УЖЕ запушил (ОПАСНО - переписывает историю!)
git commit --amend -m "Новое сообщение"
git push --force-with-lease origin feature-branch
```

### Проблема: Merge conflict

```bash
# 1. Увидеть файлы с конфликтами
git status

# 2. Открыть файлы, найти маркеры конфликта:
# <<<<<<< HEAD
# ... ваши изменения ...
# =======
# ... их изменения ...
# >>>>>>> branch-name

# 3. Разрешить конфликты вручную

# 4. Добавить разрешенные файлы
git add resolved-file.js

# 5. Завершить merge
git commit

# Или отменить merge
git merge --abort
```

### Проблема: Нужно перенести коммит из другой ветки

```bash
# Cherry-pick конкретного коммита
git checkout target-branch
git cherry-pick <commit-hash>

# Cherry-pick нескольких коммитов
git cherry-pick <hash1> <hash2> <hash3>

# Cherry-pick диапазона
git cherry-pick <start-hash>^..<end-hash>
```

### Проблема: Ошибочно запушил секреты

```bash
# 1. НЕМЕДЛЕННО удалить секрет из файла
git add file-with-secret
git commit -m "fix(security): remove leaked secret"
git push

# 2. СМЕНИТЬ секрет в сервисе

# 3. Очистить историю (если нужно)
# Использовать git-filter-repo или BFG Repo-Cleaner
git filter-repo --path secret-file --invert-paths

# 4. Force push (ТОЛЬКО если уверены)
git push --force-with-lease
```

### Проблема: Нужно откатить deployment

```bash
# 1. Найти последний стабильный коммит
git log --oneline

# 2. Создать revert commit
git revert <bad-commit-hash>

# 3. Push revert
git push origin main
```

### Проблема: Develop устарел относительно main

```bash
# Синхронизировать develop с main
git checkout develop
git merge --no-ff main
git push origin develop
```

---

## Чеклист перед коммитом

Используйте перед каждым коммитом:

- [ ] ✅ Код работает локально
- [ ] ✅ Тесты проходят (`python3 test_build.py`)
- [ ] ✅ Build успешен (`python3 build.py`)
- [ ] ✅ Нет `console.log` / debug кода
- [ ] ✅ Commit message следует конвенции
- [ ] ✅ Изменения атомарны (один логический unit)
- [ ] ✅ Нет чувствительных данных (API keys, пароли)
- [ ] ✅ `.gitignore` обновлен если нужно
- [ ] ✅ Документация обновлена если нужно
- [ ] ✅ Код review-ready (читаемый, понятный)

---

## Чеклист перед релизом

Используйте перед merge develop → main:

- [ ] ✅ Все фичи протестированы
- [ ] ✅ Все баги исправлены
- [ ] ✅ Тесты проходят на 100%
- [ ] ✅ Build проходит без ошибок и предупреждений
- [ ] ✅ Версия обновлена в `WEBSITE_CONTENT.md`
- [ ] ✅ CHANGELOG обновлен (если есть)
- [ ] ✅ Документация актуальна
- [ ] ✅ Нет TODO/FIXME в критических местах
- [ ] ✅ Проверено на всех устройствах (mobile/tablet/desktop)
- [ ] ✅ Проверено в разных браузерах
- [ ] ✅ SEO meta теги актуальны
- [ ] ✅ Создан PR для review
- [ ] ✅ Approval получен (если работа в команде)

---

## Ресурсы и документация

### Внутренние документы
- `GIT_WORKFLOW.md` - Детальный workflow
- `GIT_SETUP.md` - Инструкции по настройке
- `GIT_QUICKSTART.md` - Быстрый старт
- `PROJECT_KNOWLEDGE_GRAPH.json` - Граф знаний проекта

### Внешние ресурсы
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

---

## Changelog архитектуры

### v2.0 (2025-10-26)
- ✅ Полная система hooks
- ✅ GitHub templates (PR, Issues)
- ✅ Детальная документация
- ✅ Автоматизация через aliases
- ✅ Защита protected branches

### v1.0 (2025-10-24)
- Базовая Git структура
- Commit conventions
- Простой pre-commit hook

---

**Создано**: 2025-10-26  
**Обновлено**: 2025-10-26  
**Автор**: AI Architecture System  
**Проект**: paris-2026  
**Статус**: ✅ Production Ready

