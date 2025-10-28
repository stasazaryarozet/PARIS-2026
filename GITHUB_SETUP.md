# GitHub Setup Guide
## Branch Protection & PR Workflow Configuration

**Версия**: 1.0  
**Дата**: 28 октября 2025  
**Для проекта**: paris-2026

---

## 📋 Содержание

1. [Branch Protection Rules](#branch-protection-rules)
2. [GitHub Actions](#github-actions)
3. [PR Workflow Setup](#pr-workflow-setup)
4. [GitHub CLI Configuration](#github-cli-configuration)

---

## 🛡️ Branch Protection Rules

### Настройка для `main` branch

#### Шаги:

1. **Перейти в Settings**
   ```
   Repository → Settings → Branches → Add branch protection rule
   ```

2. **Branch name pattern**
   ```
   main
   ```

3. **Правила защиты**:

   #### ✅ Require a pull request before merging
   - ☑ **Требовать Pull Request** перед слиянием
   - Настройки:
     - Required approvals: `0` (для solo dev) или `1+` (для team)
     - ☑ Dismiss stale pull request approvals when new commits are pushed
     - ☐ Require review from Code Owners (опционально)

   #### ✅ Require status checks to pass before merging
   - ☑ **Требовать успешные проверки** перед merge
   - Выбрать checks:
     - `validate` - Validate content.js generation
     - ☑ Require branches to be up to date before merging

   #### ✅ Require conversation resolution before merging
   - ☑ Все комментарии в PR должны быть resolved

   #### ⚠️ Дополнительные опции (опционально):
   - ☐ Require signed commits
   - ☐ Require linear history (squash/rebase only)
   - ☐ Require deployments to succeed before merging

   #### ⚙️ Правила для administrators:
   - **Solo dev**: ☐ Include administrators (можно обходить правила)
   - **Team**: ☑ Include administrators (все следуют правилам)

4. **Сохранить**: Кнопка `Create` внизу страницы

---

### Настройка для `develop` branch

#### Шаги:

1. **Branch name pattern**: `develop`

2. **Правила защиты** (более мягкие):

   #### ⚠️ Restrict deletions
   - ☑ Нельзя удалить ветку

   #### ⚠️ Restrict force pushes
   - ☑ Нельзя делать force push

   #### Опционально:
   - ☑ Require status checks to pass (те же, что для main)
   - ☐ Require pull request (для team, не обязательно для solo dev)

---

## 🤖 GitHub Actions

### Созданные workflows:

#### 1. `.github/workflows/validate.yml`

**Триггеры**:
- Pull Requests → `main` или `develop`
- Push → `main` или `develop`

**Jobs**:
1. **validate** - Проверка сборки
   - Запуск `build.py`
   - Запуск `test_build.py`
   - Проверка синхронизации `content.js`
   - Валидация commit messages (для PR)

2. **build-info** - Информация о сборке
   - Показывает последний тег
   - Показывает codename
   - Выводит в GitHub Summary

**Преимущества**:
- ✅ Не зависает (в отличие от local pre-push hook)
- ✅ Логи доступны в GitHub UI
- ✅ Блокирует merge при ошибках
- ✅ Работает параллельно для всех PR

---

## 🔄 PR Workflow Setup

### Установка GitHub CLI

#### macOS:
```bash
brew install gh
```

#### Аутентификация:
```bash
gh auth login
# Выбрать: GitHub.com → HTTPS → Login with browser
```

---

### Workflow: Feature Development

#### 1. Создание feature branch
```bash
# Убедиться, что develop актуален
git checkout develop
git pull origin develop

# Создать feature branch
git checkout -b feature/my-feature
```

#### 2. Разработка и коммиты
```bash
# Работа над feature...
git add .
git commit -m "feat(scope): add new feature"

# Push в origin
git push -u origin feature/my-feature
```

#### 3. Создание Pull Request
```bash
# Создать PR в develop
gh pr create \
  --base develop \
  --title "feat: Add new feature" \
  --body "Description of changes..."

# Или интерактивно:
gh pr create
```

#### 4. Review и Merge
```bash
# Посмотреть статус PR
gh pr status

# Посмотреть checks
gh pr checks

# Merge после approval
gh pr merge --auto --squash
# Или: --merge (обычный merge) / --rebase (rebase)
```

---

### Workflow: Hotfix to Production

#### 1. Создание hotfix branch из main
```bash
git checkout main
git pull origin main

# Создать hotfix branch
git checkout -b hotfix/critical-bug
```

#### 2. Fix и коммит
```bash
# Исправление бага...
git add .
git commit -m "fix(critical): resolve production bug"

git push -u origin hotfix/critical-bug
```

#### 3. PR в main (минуя develop)
```bash
# PR напрямую в main
gh pr create \
  --base main \
  --title "hotfix: Critical bug fix" \
  --label "hotfix"

# Merge после checks
gh pr merge --squash
```

#### 4. Обратный merge в develop
```bash
git checkout develop
git merge main
git push origin develop
```

---

### Workflow: Release to Production

#### 1. Убедиться, что develop готов
```bash
git checkout develop
git pull origin develop

# Запустить локальные тесты
python3 test_build.py
```

#### 2. Создать PR: develop → main
```bash
gh pr create \
  --base main \
  --head develop \
  --title "release: Version X.Y.Z" \
  --body "**Release Notes:**
  
  - Feature 1
  - Feature 2
  - Bug fix 3"
```

#### 3. Review & Merge
```bash
# Проверить GitHub Actions
gh pr checks

# Merge в main (после approval)
gh pr merge --squash

# Автоматически:
# - GitHub Pages задеплоится
# - (Опционально) auto_tag.sh создаст тег
```

---

## 📦 Semantic Versioning & Tagging

### Автоматическое создание тегов

#### Опция 1: Post-merge hook (локально)

Создать `.git/hooks/post-merge`:
```bash
#!/bin/bash
# Автоматический тег после merge в main

if [ "$(git branch --show-current)" = "main" ]; then
    bash tools/auto_tag.sh
fi
```

```bash
chmod +x .git/hooks/post-merge
```

#### Опция 2: Ручное создание тегов

```bash
# После merge в main
git checkout main
git pull origin main

# Запустить auto_tag.sh
bash tools/auto_tag.sh

# Push тега
git push origin <new-tag>
```

#### Опция 3: GitHub Actions (будущее)

Создать workflow для автоматического тегирования после merge PR в main.

---

## 🎯 Best Practices

### Commit Messages

Всегда используйте **Conventional Commits**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: Новая функциональность
- `fix`: Исправление бага
- `docs`: Документация
- `style`: Форматирование (не CSS!)
- `refactor`: Рефакторинг кода
- `test`: Добавление тестов
- `chore`: Обслуживание (deps, config)
- `build`: Системы сборки
- `ci`: CI/CD конфигурация
- `perf`: Оптимизация производительности

### PR Guidelines

1. **Один PR = одна фича/fix**
2. **Описание PR**:
   - Что изменено
   - Почему изменено
   - Как протестировано
3. **Размер**: Старайтесь держать PR <500 строк
4. **Скриншоты**: Для UI изменений добавляйте скриншоты
5. **Breaking changes**: Явно указывать в description

### Branch Naming

```
feature/short-description   - новая функциональность
fix/bug-description         - исправление бага
hotfix/critical-fix         - критический hotfix для production
docs/what-documented        - документация
refactor/what-refactored    - рефакторинг
experiment/what-testing     - эксперименты (можно удалить без merge)
```

---

## ✅ Verification Checklist

После настройки убедитесь:

- [ ] Branch protection для `main` активна
- [ ] GitHub Actions workflow работает
- [ ] GitHub CLI установлен и аутентифицирован
- [ ] `tools/auto_tag.sh` исполняемый (`chmod +x`)
- [ ] Тестовый PR проходит все checks
- [ ] Merge в main блокируется без PR (если enabled)
- [ ] Теги создаются корректно

---

## 🔧 Troubleshooting

### Problem: GitHub Actions не запускается

**Solution**:
```bash
# Проверить наличие workflow файлов
ls -la .github/workflows/

# Проверить права доступа в Settings → Actions
# Должно быть: "Allow all actions and reusable workflows"
```

### Problem: PR не создается через gh CLI

**Solution**:
```bash
# Переаутентификация
gh auth logout
gh auth login

# Проверка статуса
gh auth status
```

### Problem: Branch protection не работает

**Solution**:
- Проверить, что не включено "Include administrators" (если solo dev)
- Проверить, что используете правильную кнопку "Merge pull request" в UI
- Проверить настройки в Settings → Branches

---

## 📚 Дополнительные ресурсы

- [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [GitHub Actions](https://docs.github.com/en/actions)
- [GitHub CLI](https://cli.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

---

**Создано**: 28 октября 2025  
**Статус**: ✅ Ready for implementation  
**Следующий шаг**: Включить branch protection для main

