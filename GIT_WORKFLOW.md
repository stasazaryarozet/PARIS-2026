# Git Workflow Architecture
## Архитектура работы с Git для проекта paris-2026

---

## Оглавление

1. [Философия](#философия)
2. [Структура веток](#структура-веток)
3. [Commit Conventions](#commit-conventions)
4. [Git Hooks](#git-hooks)
5. [Workflow сценарии](#workflow-сценарии)
6. [Правила слияния](#правила-слияния)
7. [Защита веток](#защита-веток)
8. [Теги и версионирование](#теги-и-версионирование)
9. [Команды для ежедневной работы](#команды-для-ежедневной-работы)

---

## Философия

### Принципы

1. **Атомарность**: Один коммит = одно логическое изменение
2. **Читаемость**: История должна рассказывать историю проекта
3. **Надежность**: Каждый коммит в main/production должен быть рабочим
4. **Прозрачность**: Коммиты должны быть самодокументирующимися
5. **Автоматизация**: Максимум проверок через hooks и CI/CD

### Single Source of Truth

- `main` - production-ready код
- История коммитов - источник правды о развитии проекта
- Теги - точки стабильных релизов

---

## Структура веток

### Основные ветки

```
main (production)
  ↑
  ├── develop (integration)
  ↑
  ├── feature/* (новая функциональность)
  ├── fix/* (исправления багов)
  ├── hotfix/* (критические исправления для production)
  ├── docs/* (документация)
  └── experiment/* (эксперименты, можно удалять)
```

### Описание веток

#### `main`
- **Назначение**: Production-ready код
- **Защита**: Прямые коммиты запрещены
- **Слияние**: Только через Pull Requests из `develop` или `hotfix/*`
- **Правило**: Каждый коммит в main должен быть тегирован
- **Деплой**: Автоматический деплой на GitHub Pages

#### `develop`
- **Назначение**: Интеграция feature веток
- **Защита**: Прямые коммиты нежелательны
- **Слияние**: Из `feature/*`, `fix/*`
- **Тестирование**: Все фичи должны быть протестированы перед слиянием в main

#### `feature/*`
- **Формат**: `feature/<краткое-описание>`
- **Примеры**: `feature/booking-form`, `feature/arabic-i18n`
- **Жизненный цикл**: Создается → Разработка → Merge в develop → Удаляется
- **Базируется на**: `develop`

#### `fix/*`
- **Формат**: `fix/<краткое-описание>`
- **Примеры**: `fix/rtl-direction`, `fix/mobile-menu`
- **Жизненный цикл**: Создается → Исправление → Merge в develop → Удаляется
- **Базируется на**: `develop`

#### `hotfix/*`
- **Формат**: `hotfix/<версия>-<описание>`
- **Примеры**: `hotfix/v1.2.1-critical-form-bug`
- **Жизненный цикл**: Создается из main → Исправление → Merge в main И develop → Удаляется
- **Базируется на**: `main`
- **Использование**: Только для критических багов в production

#### `docs/*`
- **Формат**: `docs/<что-документируется>`
- **Примеры**: `docs/git-workflow`, `docs/deployment`
- **Жизненный цикл**: Создается → Документирование → Merge в develop → Удаляется
- **Базируется на**: `develop`

#### `experiment/*`
- **Формат**: `experiment/<что-тестируем>`
- **Примеры**: `experiment/parallax-hero`, `experiment/animations`
- **Жизненный цикл**: Создается → Эксперимент → Merge ИЛИ Удаляется
- **Базируется на**: `develop`
- **Правило**: Может быть удалена без слияния

---

## Commit Conventions

### Формат коммита

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Типы (type)

| Тип | Описание | Пример |
|-----|----------|--------|
| `feat` | Новая функциональность | `feat(form): добавить валидацию email` |
| `fix` | Исправление бага | `fix(i18n): исправить RTL для арабского` |
| `docs` | Документация | `docs: обновить README` |
| `style` | Стили, форматирование | `style: увеличить размер h2` |
| `refactor` | Рефакторинг кода | `refactor(build): упростить парсер` |
| `perf` | Оптимизация | `perf(images): сжать og-image.jpg` |
| `test` | Тесты | `test: добавить тесты для build.py` |
| `build` | Build система | `build: настроить GitHub Actions` |
| `ci` | CI/CD | `ci: добавить pre-commit hook` |
| `chore` | Рутина | `chore: обновить .gitignore` |
| `revert` | Откат | `revert: откатить коммит abc123` |

### Области (scope)

- `content` - контент, тексты
- `design` - дизайн, визуальное
- `form` - форма бронирования
- `i18n` - интернационализация
- `build` - build система
- `deps` - зависимости
- `config` - конфигурация
- `docs` - документация

### Subject (заголовок)

✅ **Правильно:**
```
feat(form): добавить валидацию телефона
fix(design): исправить overflow на мобильных
docs: обновить инструкции по деплою
```

❌ **Неправильно:**
```
Добавил валидацию (не imperative mood)
fixed bug (не информативно)
WIP (не коммитить незавершенное)
Обновление. (точка в конце)
```

### Body (тело)

Используется когда нужно больше контекста:

```
feat(form): добавить валидацию телефона

Добавлена клиентская валидация для поля телефона:
- Проверка формата (международный)
- Проверка на пустое значение
- Визуальная индикация ошибок

Это улучшает UX и снижает количество некорректных заявок.
```

### Footer (подвал)

Для связи с issues и breaking changes:

```
fix(api): изменить формат даты в API

BREAKING CHANGE: Формат даты изменен с DD/MM/YYYY на ISO 8601

Closes #123
Refs #456
```

---

## Git Hooks

### Pre-commit Hook

**Расположение**: `.git/hooks/pre-commit`

**Выполняет**:
1. Проверка синтаксиса (Python, JS)
2. Запуск тестов
3. Проверка стиля кода
4. Проверка commit message (если есть)

**Установка**:
```bash
chmod +x .git/hooks/pre-commit
```

### Commit-msg Hook

**Расположение**: `.git/hooks/commit-msg`

**Выполняет**:
1. Валидация формата commit message
2. Проверка на запрещенные слова (WIP, TODO в production)

### Pre-push Hook

**Расположение**: `.git/hooks/pre-push`

**Выполняет**:
1. Запуск полного набора тестов
2. Проверка что не пушим в protected ветки напрямую
3. Проверка что build проходит

---

## Workflow сценарии

### Сценарий 1: Добавление новой фичи

```bash
# 1. Обновить develop
git checkout develop
git pull origin develop

# 2. Создать feature ветку
git checkout -b feature/booking-form

# 3. Разработка (коммиты по мере готовности)
git add .
git commit -m "feat(form): добавить структуру формы"
git commit -m "feat(form): добавить валидацию полей"
git commit -m "feat(form): интегрировать с Formspree API"

# 4. Пуш ветки
git push origin feature/booking-form

# 5. Создать Pull Request: feature/booking-form → develop
# 6. Code review
# 7. Merge в develop (squash или merge commit)
# 8. Удалить feature ветку
git branch -d feature/booking-form
git push origin --delete feature/booking-form
```

### Сценарий 2: Исправление бага

```bash
# 1. Создать fix ветку из develop
git checkout develop
git pull origin develop
git checkout -b fix/mobile-menu-overlap

# 2. Исправление
git add style.css
git commit -m "fix(design): исправить перекрытие меню на мобильных"

# 3. Пуш и PR
git push origin fix/mobile-menu-overlap
# Создать PR → develop → Merge → Удалить ветку
```

### Сценарий 3: Критический hotfix для production

```bash
# 1. Создать hotfix ветку из main
git checkout main
git pull origin main
git checkout -b hotfix/v1.0.1-form-submission-error

# 2. Исправление
git add index.html
git commit -m "fix(form): исправить ошибку отправки формы"

# 3. Merge в main
git checkout main
git merge --no-ff hotfix/v1.0.1-form-submission-error
git tag -a v1.0.1 -m "Hotfix: исправление формы"
git push origin main --tags

# 4. Merge в develop (чтобы исправление попало в develop)
git checkout develop
git merge --no-ff hotfix/v1.0.1-form-submission-error
git push origin develop

# 5. Удалить hotfix ветку
git branch -d hotfix/v1.0.1-form-submission-error
git push origin --delete hotfix/v1.0.1-form-submission-error
```

### Сценарий 4: Релиз из develop в main

```bash
# 1. Убедиться что develop готов к релизу
git checkout develop
git pull origin develop
# Запустить все тесты
# Проверить build

# 2. Создать release ветку (опционально)
git checkout -b release/v1.1.0

# 3. Финальные правки (версии, changelog)
git commit -m "chore(release): подготовка версии v1.1.0"

# 4. Merge в main
git checkout main
git merge --no-ff release/v1.1.0
git tag -a v1.1.0 -m "Release v1.1.0: Добавлена арабская локализация"
git push origin main --tags

# 5. Merge обратно в develop
git checkout develop
git merge --no-ff release/v1.1.0
git push origin develop

# 6. Удалить release ветку
git branch -d release/v1.1.0
```

### Сценарий 5: Быстрые правки контента

Для небольших правок контента можно работать напрямую с develop:

```bash
git checkout develop
git pull origin develop

# Редактирование
git add WEBSITE_CONTENT.md
git commit -m "docs(content): обновить описание программы дня 2"

git push origin develop
```

---

## Правила слияния

### Merge vs Squash vs Rebase

#### Merge (--no-ff)
**Использовать для**: Слияния долгоживущих веток (feature → develop, develop → main)

```bash
git merge --no-ff feature/booking-form
```

✅ **Преимущества**: Сохраняет всю историю, видна граница фичи
❌ **Недостатки**: Может создать много merge коммитов

#### Squash
**Использовать для**: Слияния feature веток с множеством WIP коммитов

```bash
git merge --squash feature/experiment
git commit -m "feat: добавить экспериментальную анимацию"
```

✅ **Преимущества**: Чистая история, один коммит на фичу
❌ **Недостатки**: Теряется детальная история разработки

#### Rebase
**Использовать для**: Обновления feature ветки с последними изменениями develop

```bash
git checkout feature/my-feature
git rebase develop
```

✅ **Преимущества**: Линейная история, легко читать
❌ **Недостатки**: Переписывает историю (не для shared веток)

### Рекомендации

- **feature → develop**: merge --no-ff или squash (зависит от качества коммитов)
- **develop → main**: merge --no-ff (всегда)
- **hotfix → main**: merge --no-ff
- **Обновление feature ветки**: rebase на develop

---

## Защита веток

### Protected Branches: main

**Правила для main**:
1. ❌ Прямые push запрещены
2. ✅ Только через Pull Requests
3. ✅ Требуется code review (если работа в команде)
4. ✅ Все CI checks должны пройти
5. ✅ Squash commits опционально

### Protected Branches: develop

**Правила для develop**:
1. ❌ Force push запрещен
2. ✅ Прямые коммиты разрешены (только для minor правок)
3. ✅ Feature ветки через PR предпочтительнее

### Настройка защиты на GitHub

```
Settings → Branches → Add rule

Branch name pattern: main

☑ Require pull request reviews before merging
☑ Require status checks to pass before merging
☑ Require branches to be up to date before merging
☑ Include administrators
```

---

## Теги и версионирование

### Semantic Versioning

Формат: `vMAJOR.MINOR.PATCH`

- **MAJOR**: Несовместимые изменения API
- **MINOR**: Новая функциональность (обратно совместимая)
- **PATCH**: Исправления багов

**Примеры**:
- `v1.0.0` - Первый публичный релиз
- `v1.1.0` - Добавлена арабская локализация
- `v1.1.1` - Исправлен баг в форме
- `v2.0.0` - Полный редизайн (breaking change)

### Создание тегов

```bash
# Lightweight tag (для экспериментов)
git tag v1.0.0

# Annotated tag (для релизов - РЕКОМЕНДУЕТСЯ)
git tag -a v1.0.0 -m "Release v1.0.0: Первый стабильный релиз"

# Подписанный тег (для важных релизов)
git tag -s v1.0.0 -m "Release v1.0.0: Production ready"

# Push тегов
git push origin v1.0.0
git push origin --tags  # все теги
```

### Список тегов

```bash
# Все теги
git tag

# Теги с паттерном
git tag -l "v1.*"

# Информация о теге
git show v1.0.0
```

### Удаление тегов

```bash
# Локально
git tag -d v1.0.0

# На remote
git push origin --delete v1.0.0
```

---

## Команды для ежедневной работы

### Быстрый старт новой фичи

```bash
# Алиас для быстрого создания feature ветки
git config alias.feat '!f() { git checkout develop && git pull && git checkout -b feature/$1; }; f'

# Использование
git feat booking-form
```

### Синхронизация с upstream

```bash
# Обновить develop
git checkout develop
git pull origin develop

# Обновить feature ветку
git checkout feature/my-feature
git rebase develop
```

### Просмотр истории

```bash
# Красивый лог
git log --oneline --graph --decorate --all

# Алиас
git config alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Использование
git lg
```

### Откат изменений

```bash
# Откат uncommitted изменений
git restore <file>

# Откат staged изменений
git restore --staged <file>

# Откат последнего коммита (сохранить изменения)
git reset --soft HEAD~1

# Откат последнего коммита (удалить изменения)
git reset --hard HEAD~1

# Откат specific commit
git revert <commit-hash>
```

### Stash (отложить изменения)

```bash
# Сохранить изменения
git stash

# Сохранить с описанием
git stash save "WIP: booking form validation"

# Список stashes
git stash list

# Применить последний stash
git stash apply

# Применить и удалить
git stash pop

# Удалить stash
git stash drop stash@{0}

# Очистить все
git stash clear
```

### Cherry-pick (взять commit из другой ветки)

```bash
# Взять конкретный коммит
git cherry-pick <commit-hash>

# Взять несколько коммитов
git cherry-pick <hash1> <hash2>

# Взять диапазон
git cherry-pick <hash1>^..<hash2>
```

---

## Полезные алиасы

Добавьте в `~/.gitconfig`:

```ini
[alias]
    # Shortcuts
    co = checkout
    br = branch
    ci = commit
    st = status
    unstage = restore --staged
    
    # Logs
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    ls = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate
    ll = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --numstat
    
    # Branching
    feat = "!f() { git checkout develop && git pull && git checkout -b feature/$1; }; f"
    fix = "!f() { git checkout develop && git pull && git checkout -b fix/$1; }; f"
    hot = "!f() { git checkout main && git pull && git checkout -b hotfix/$1; }; f"
    
    # Cleanup
    cleanup = "!git branch --merged | grep -v '\\*\\|main\\|develop' | xargs -n 1 git branch -d"
    
    # Quick commits
    ca = commit --amend --no-edit
    caa = commit -a --amend --no-edit
    
    # Diffs
    d = diff
    ds = diff --staged
    
    # Undo
    undo = reset --soft HEAD~1
    
    # Show what I did today
    today = log --since='1 day ago' --oneline --author=\"$(git config user.name)\"
```

---

## Troubleshooting

### Проблема: Случайно закоммитил в main

```bash
# 1. Создать ветку с изменениями
git branch feature/accidental-commit

# 2. Откатить main
git reset --hard HEAD~1

# 3. Переключиться на ветку
git checkout feature/accidental-commit

# 4. Сделать PR из ветки
```

### Проблема: Нужно изменить последний commit message

```bash
# Если еще не запушил
git commit --amend -m "Новое сообщение"

# Если уже запушил (ОПАСНО - переписывает историю)
git commit --amend -m "Новое сообщение"
git push --force-with-lease
```

### Проблема: Merge conflict

```bash
# 1. Посмотреть конфликты
git status

# 2. Открыть файлы, разрешить конфликты
# Искать маркеры: <<<<<<< HEAD, =======, >>>>>>>

# 3. После разрешения
git add <resolved-files>
git commit

# Или отменить merge
git merge --abort
```

### Проблема: Нужно удалить файл из истории (секреты)

```bash
# Использовать git-filter-repo (безопаснее чем filter-branch)
git filter-repo --path <file-to-remove> --invert-paths

# Или BFG Repo-Cleaner
java -jar bfg.jar --delete-files <file-pattern> .
```

---

## Чеклист перед коммитом

- [ ] Код работает локально
- [ ] Тесты проходят
- [ ] Нет console.log / debugging кода
- [ ] Commit message соответствует конвенции
- [ ] Изменения атомарны (один логический unit)
- [ ] Нет чувствительных данных (пароли, API keys)
- [ ] .gitignore обновлен если нужно
- [ ] Документация обновлена если нужно

---

## Ресурсы

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

---

**Создано**: 2025-10-26  
**Версия**: 1.0  
**Проект**: paris-2026

