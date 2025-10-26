# Git Quickstart Guide
## Быстрый старт для работы с Git в проекте paris-2026

---

## Первоначальная настройка

### 1. Настройка commit message template

```bash
git config commit.template .gitmessage
```

### 2. Настройка автора

```bash
git config user.name "Ваше Имя"
git config user.email "your.email@example.com"
```

### 3. Полезные алиасы

```bash
# Добавить алиасы
git config alias.co checkout
git config alias.br branch
git config alias.ci commit
git config alias.st status
git config alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Алиасы для branching
git config alias.feat '!f() { git checkout develop && git pull && git checkout -b feature/$1; }; f'
git config alias.fix '!f() { git checkout develop && git pull && git checkout -b fix/$1; }; f'
```

### 4. Проверка hooks

```bash
# Проверить что hooks установлены и исполняемы
ls -la .git/hooks/ | grep -E "(pre-commit|commit-msg|pre-push)"

# Если не исполняемы:
chmod +x .git/hooks/pre-commit .git/hooks/commit-msg .git/hooks/pre-push
```

---

## Ежедневные команды

### Начало работы

```bash
# Обновить develop
git checkout develop
git pull origin develop

# Создать feature ветку
git checkout -b feature/my-feature
# или с алиасом:
git feat my-feature
```

### Работа с изменениями

```bash
# Статус
git status
# или алиас:
git st

# Добавить файлы
git add <файл>
git add .  # все файлы

# Коммит
git commit
# Откроется редактор с шаблоном

# Быстрый коммит
git commit -m "feat(design): добавить новую кнопку"

# Изменить последний коммит
git commit --amend
```

### Просмотр истории

```bash
# Красивый лог
git lg
# или полная команда:
git log --graph --oneline --all

# Что я сделал сегодня
git log --since="1 day ago" --author="$(git config user.name)"

# Изменения в файле
git log -p <файл>
```

### Синхронизация

```bash
# Обновить текущую ветку
git pull

# Обновить feature ветку с develop
git checkout feature/my-feature
git rebase develop

# Push
git push origin feature/my-feature

# Первый push новой ветки
git push -u origin feature/my-feature
```

---

## Типовые сценарии

### Сценарий 1: Новая фича

```bash
# 1. Создать ветку
git checkout develop
git pull
git checkout -b feature/booking-form

# 2. Работа
# ... редактирование файлов ...

# 3. Коммиты
git add .
git commit  # используйте шаблон

# 4. Push
git push -u origin feature/booking-form

# 5. Создать Pull Request на GitHub
# feature/booking-form → develop

# 6. После merge - удалить ветку
git checkout develop
git pull
git branch -d feature/booking-form
```

### Сценарий 2: Быстрое исправление

```bash
# 1. Создать fix ветку
git checkout develop
git pull
git checkout -b fix/mobile-layout

# 2. Исправить
# ... правка файлов ...

# 3. Коммит и push
git add .
git commit -m "fix(design): исправить layout на мобильных"
git push -u origin fix/mobile-layout

# 4. Pull Request → merge → удалить ветку
```

### Сценарий 3: Отложить работу (stash)

```bash
# Срочно нужно переключиться на другую задачу

# Отложить изменения
git stash save "WIP: booking form validation"

# Переключиться на другую ветку
git checkout other-branch

# ... работа ...

# Вернуться
git checkout feature/my-feature

# Восстановить изменения
git stash pop
```

### Сценарий 4: Откат изменений

```bash
# Откатить незакоммиченные изменения
git restore <файл>

# Откатить все незакоммиченные
git restore .

# Убрать файл из staging
git restore --staged <файл>

# Откатить последний коммит (сохранить изменения)
git reset --soft HEAD~1

# Откатить последний коммит (удалить изменения)
git reset --hard HEAD~1
```

---

## Commit Message Cheatsheet

### Формат

```
<type>(<scope>): <subject>

<body (опционально)>

<footer (опционально)>
```

### Типы

- `feat` - новая функциональность
- `fix` - исправление бага
- `docs` - документация
- `style` - стили, форматирование
- `refactor` - рефакторинг
- `perf` - оптимизация
- `test` - тесты
- `build` - build система
- `ci` - CI/CD
- `chore` - рутинные задачи

### Примеры

```bash
feat(form): добавить валидацию email
fix(i18n): исправить RTL для арабского
docs: обновить README с инструкциями
style(design): увеличить размер заголовков
refactor(build): упростить парсер markdown
perf(images): оптимизировать og-image
test(build): добавить тесты для генератора
chore: обновить .gitignore
```

---

## Работа с ветками

### Создание

```bash
# Из develop
git checkout develop
git checkout -b feature/new-feature

# С алиасом
git feat new-feature
git fix bug-name
```

### Переключение

```bash
git checkout <branch-name>

# Создать и переключиться
git checkout -b <new-branch>
```

### Просмотр

```bash
# Локальные ветки
git branch

# Все ветки (включая remote)
git branch -a

# С последним коммитом
git branch -v
```

### Удаление

```bash
# Локально (если смержена)
git branch -d feature/old-feature

# Принудительно
git branch -D feature/old-feature

# На remote
git push origin --delete feature/old-feature
```

### Переименование

```bash
# Переименовать текущую ветку
git branch -m new-name

# Переименовать другую ветку
git branch -m old-name new-name
```

---

## Разрешение конфликтов

### Когда конфликт возникает

```bash
# При merge или rebase
git merge feature/other
# CONFLICT in file.html
```

### Как разрешить

```bash
# 1. Открыть файлы с конфликтами
git status  # покажет конфликтующие файлы

# 2. Найти маркеры конфликта
<<<<<<< HEAD
Ваши изменения
=======
Чужие изменения
>>>>>>> feature/other

# 3. Разрешить вручную
# Оставить нужный вариант или объединить

# 4. Добавить разрешенные файлы
git add <resolved-file>

# 5. Завершить merge
git commit
# или для rebase:
git rebase --continue
```

### Отменить merge/rebase

```bash
# Отменить merge
git merge --abort

# Отменить rebase
git rebase --abort
```

---

## Полезные команды

### Поиск

```bash
# Найти в истории коммитов
git log --grep="booking form"

# Найти изменения в файле
git log -S "search term" -- path/to/file

# Кто изменил строку
git blame <файл>
```

### Diff

```bash
# Изменения в working directory
git diff

# Изменения в staging
git diff --staged

# Между ветками
git diff develop..feature/my-feature

# Конкретный файл
git diff <файл>
```

### Clean

```bash
# Показать что будет удалено
git clean -n

# Удалить untracked файлы
git clean -f

# Удалить включая директории
git clean -fd
```

### Remote

```bash
# Показать remotes
git remote -v

# Добавить remote
git remote add <name> <url>

# Обновить URL
git remote set-url origin <new-url>

# Удалить remote
git remote remove <name>
```

---

## Troubleshooting

### Проблема: "Your branch is behind"

```bash
# Решение 1: Pull
git pull

# Решение 2: Pull с rebase (чище история)
git pull --rebase
```

### Проблема: Случайно закоммитил не в ту ветку

```bash
# 1. Создать ветку с текущими изменениями
git branch feature/correct-branch

# 2. Откатить текущую ветку
git reset --hard HEAD~1

# 3. Переключиться на правильную
git checkout feature/correct-branch
```

### Проблема: Нужно изменить commit message

```bash
# Последний коммит
git commit --amend

# Старый коммит (интерактивный rebase)
git rebase -i HEAD~3
# Изменить 'pick' на 'reword' для нужного коммита
```

### Проблема: Нужно объединить несколько коммитов

```bash
# Интерактивный rebase
git rebase -i HEAD~3

# Изменить 'pick' на 'squash' для коммитов которые нужно объединить
# Сохранить и закрыть редактор
```

### Проблема: Отменить последний push (ОПАСНО)

```bash
# Откатить локально
git reset --hard HEAD~1

# Force push (только для feature веток!)
git push --force-with-lease
```

---

## Чеклист перед коммитом

- [ ] Код работает локально
- [ ] Нет console.log / debugging кода
- [ ] Commit message соответствует конвенции
- [ ] Изменения атомарны
- [ ] Нет чувствительных данных

---

## Чеклист перед push

- [ ] Все коммиты имеют понятные сообщения
- [ ] Build проходит (если есть)
- [ ] Тесты проходят (если есть)
- [ ] Нет незакоммиченных изменений
- [ ] Ветка обновлена с develop

---

## Полезные ссылки

- [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) - Полная документация
- [.gitmessage](./.gitmessage) - Шаблон commit message
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Book](https://git-scm.com/book/en/v2)

---

**Обновлено**: 2025-10-26

