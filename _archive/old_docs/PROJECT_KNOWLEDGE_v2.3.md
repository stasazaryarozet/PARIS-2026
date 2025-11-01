---
meta:
  project: paris-2026
  version: 2.2-ig-strategy
  created: 2025-10-26
  last_updated: 2025-10-29
  format: Markdown + YAML
  purpose: Единый источник знаний о проекте для AI-агентов и людей
  encoding: UTF-8
---

# PROJECT KNOWLEDGE — Единый источник правды

**Версия:** 2.2 (IG Strategy Integrated)  
**Дата:** 29 октября 2025  
**Статус:** Canonical source of truth

---

## 0. КАК ЧИТАТЬ ЭТОТ ДОКУМЕНТ

**Для AI-агентов:** Прочитать полностью при загрузке контекста. Все критические правила, паттерны и исходники здесь.

**Для людей:** Навигация по якорям. Структура: мета-уровень → операционный уровень → исходники.

**Формат:** Markdown (человекочитаемость) + YAML-блоки (структурированность) + прямые цитаты (достоверность).

---

# I. МЕТА-УРОВЕНЬ: ОНТОЛОГИЯ ПРОЕКТА

## 1. СУЩНОСТЬ ПРОЕКТА

```yaml
essence:
  id: project_essence
  name: Кураторский тур Париж 2026
  tagline: "Индивидуальный почерк ар-деко. 100 лет"
  format: Премиальный 4-дневный тур с экспертами
  dates: 15–18+ января 2026
  price: 1550 €
  capacity: до 12 человек
  
  core_values:
    - экспертность
    - камерность
    - атмосфера
    - индивидуальный_подход
  
  keywords:
    - ар-деко
    - Париж
    - кураторская программа
    - малая группа
    - премиум
    - фактуры
    - материалы
```

### Философия программы

> **Ольга Розет (Recording 14):**  
> "Мы будем в интерьерах смотреть секреты мастеров. Соотношения фактуры текстур, тонкости цвета, которые не видны ни в одной публикации."

**Центральная идея:** Индивидуальный почерк — у каждого мастера свой способ работы с материалом.

**Сквозная тема:** Эволюция отношений "Материал — Человек" от 1920-х к 1950-м:
- **Рульманн (1920-е):** Материал как статус
- **Эйлин Грей (1930-е):** Материал как адаптация
- **Аалто (1950-е):** Материал как забота
- **Денье (2010-е):** Материал как атмосфера

**Каноническая связка Фигура—Концепция (Instagram Campaign, Oct 2025):**
- **Демонстрация** → Рульманн и Легре
- **Атмосфера** → Денье
- **Забота** → Грей и Аалто

**Нарративная ось:** "Человечность" (введена в Stories, Oct 28):
- От индивидуального почерка к человечности подхода
- От демонстрации материала к заботе о человеке
- Эргономика = забота (Аалто)

---

## 2. АРХИТЕКТУРА ПРОЕКТА

```yaml
architecture:
  pattern: single_source_of_truth
  
  content_layer:
    source_of_truth: WEBSITE_CONTENT.md
    generated: content.js
    rule: "WEBSITE_CONTENT.md → build.py → content.js"
    critical: "Никогда не редактировать content.js вручную"
    philosophy: "Markdown как единственный источник правды"
  
  presentation_layer:
    structure: index.html
    styling: style.css
    behavior: "inline JavaScript в index.html"
    pattern: "Чистый HTML/CSS/JS без фреймворков"
  
  bilingual_support:
    languages: [ru, ar]
    content_files:
      - WEBSITE_CONTENT.md
      - WEBSITE_CONTENT_AR.md
    switching: "Кнопка переключения, localStorage"
    direction: "RTL для арабского, LTR для русского"
  
  principles:
    - "Простота превыше сложности"
    - "Один источник правды для контента"
    - "Автоматическая генерация, не ручное редактирование"
    - "Валидация перед каждым коммитом"
```

### Рабочий процесс

```yaml
workflow:
  deployment_cycle:
    - "1. Редактирование WEBSITE_CONTENT.md"
    - "2. python3 build.py (генерация content.js)"
    - "3. Валидация и тесты"
    - "4. git add, commit, push"
    - "5. Автодеплой на GitHub Pages"
  
  versioning:
    format: "v{number}-{description}"
    examples:
      - v179-hide-badge
      - handshake-v4
    stored_in: "WEBSITE_CONTENT.md meta.version"
    visibility: "Скрыт от пользователей (display: none)"
  
  validation:
    pre_commit_hook: "Автоматическая регенерация content.js"
    test_suite: "test_build.py с 10 тестами"
    checks:
      - синтаксис JS
      - структура данных
      - критические элементы
```

---

## 3. ДИЗАЙН-ФИЛОСОФИЯ

```yaml
design_philosophy:
  core_principles:
    minimalism:
      description: "Минимализм без холодности"
      implementation: "Чистые линии, воздух, приглушенная палитра"
    
    elegance:
      description: "Элегантность и премиальность"
      implementation: "Качественная типографика, деликатные акценты"
    
    atmosphere:
      description: "Атмосфера важнее декоративности"
      implementation: "Настроение через типографику и пространство"
    
    restraint:
      description: "Сдержанность и вкус"
      implementation: "Меньше да лучше, каждый элемент оправдан"
  
  typography:
    heading_font: "Cormorant Garamond (serif, elegant)"
    body_font: "Inter (sans-serif, readable)"
    accent_font: "Forum (decorative, art-deco echo)"
    hierarchy: "Выразительная типографическая иерархия"
  
  color_palette:
    primary: "#E31B1B (accent red)"
    secondary: "#0A2342 (midnight blue)"
    neutral:
      - "#F8F6F3 (warm white)"
      - "#E8E4DD (soft beige)"
      - "#2C2C2C (charcoal)"
    philosophy: "Приглушенная элегантность с красным акцентом"
  
  spacing:
    principle: "Generous whitespace"
    implementation: "Воздух между секциями, не перегружать"
```

---

## 4. КОНТЕНТ-СТРАТЕГИЯ

```yaml
content_strategy:
  tone_of_voice:
    characteristics:
      - доверительный
      - экспертный
      - не продающий
      - атмосферный
    avoid:
      - маркетинговые штампы
      - восклицания
      - давление
      - преувеличения
  
  key_messages:
    expertise: "Экспертное кураторство (Розет + Логинова)"
    intimacy: "Малая группа, индивидуальный подход"
    uniqueness: "100 лет ар-деко, уникальная программа"
    atmosphere: "Фактуры, материалы, атмосфера"
  
  structure:
    hero: "Эмоциональный захват + ключевая информация"
    program: "4 дня детальной программы"
    curators: "Эксперты, их подход"
    inclusions: "Что включено"
    cta: "Booking form без агрессии"
  
  semantic_richness:
    principle: "Можно ли ощутить словами?"
    implementation: "Конкретные детали вместо абстракций"
    examples:
      - малабарское дерево
      - стеклянные кирпичи
      - фактуры
      - материалы
  
  promo_content_principle:
    name: "Без избыточности"
    rule: "Промо-текст (IG/email) должен ДОПОЛНЯТЬ посадочную, не ДУБЛИРОВАТЬ"
    exception: "Якорные фразы (даты, имена, цена) разрешены для повторения"
    rationale: "Забота о Зрителе = минимизация шума на экране"
```

### Ключевая формулировка (финальная)

> **Ольга Розет (Recording 22):**  
> "Парижские дизайнеры смешивают новое со старым. Интерьер без предметов с историей выглядит неживо."

---

## 5. КРИТИЧЕСКИЕ ПРАВИЛА

```yaml
critical_rules:
  - id: rule_001
    category: content
    rule: "WEBSITE_CONTENT.md - единственный источник правды"
    rationale: "Предотвращение рассинхронизации контента"
    enforcement: "Автоматическая регенерация content.js"
    severity: CRITICAL
  
  - id: rule_002
    category: content
    rule: "Никогда не редактировать content.js вручную"
    rationale: "Изменения будут перезаписаны при следующей генерации"
    enforcement: "Предупреждение в начале content.js"
    severity: CRITICAL
  
  - id: rule_003
    category: workflow
    rule: "Всегда запускать build.py перед коммитом"
    rationale: "Гарантия актуальности content.js"
    enforcement: "Pre-commit hook"
    severity: CRITICAL
  
  - id: rule_004
    category: communication
    rule: "Всегда отвечать на русском языке"
    rationale: "Предпочтение пользователя"
    enforcement: "Явное указание в правилах"
    severity: HIGH
  
  - id: rule_005
    category: communication
    rule: "Максимальная агентность - делать, не спрашивать"
    rationale: "Эффективность работы, доверие пользователя"
    enforcement: "Паттерн поведения"
    severity: HIGH
  
  - id: rule_006
    category: design
    rule: "Минимализм без холодности, элегантность без перегруженности"
    rationale: "Премиальное позиционирование"
    enforcement: "Ревью каждого изменения"
    severity: MEDIUM
  
  - id: rule_007
    category: content
    rule: "Избегать маркетинговых штампов и агрессивных продаж"
    rationale: "Доверительный экспертный tone of voice"
    enforcement: "Редактура и правка"
    severity: MEDIUM
  
  - id: rule_008
    category: technical
    rule: "Простота превыше сложности, нет фреймворков без необходимости"
    rationale: "Maintainability, производительность"
    enforcement: "Архитектурные решения"
    severity: HIGH
  
  - id: rule_009
    category: critical_elements
    rule: "Регистрационная форма = постоянный приоритет, проверка при каждом деплое"
    rationale: "Единственный канал конверсии, прямой revenue impact"
    enforcement: "FORM_CHECK_PROCEDURE.md (mandatory)"
    severity: CRITICAL
    created: 2025-10-28
```

---

## 6. ГРАФ ОТНОШЕНИЙ

```yaml
relationships:
  - from: project_essence
    to: design_philosophy
    type: informs
    description: "Премиальность проекта определяет минималистичный элегантный дизайн"
  
  - from: design_philosophy
    to: user_experience
    type: shapes
    description: "Дизайн-философия формирует пользовательский опыт"
  
  - from: architecture
    to: workflow
    type: enables
    description: "Архитектура определяет рабочий процесс"
  
  - from: content_strategy
    to: project_essence
    type: expresses
    description: "Контент-стратегия выражает суть проекта"
  
  - from: technical_patterns
    to: architecture
    type: implements
    description: "Технические паттерны реализуют архитектуру"
  
  - from: quality_standards
    to: workflow
    type: governs
    description: "Стандарты качества контролируют рабочий процесс"
  
  - from: communication_patterns
    to: workflow
    type: guides
    description: "Паттерны коммуникации направляют итерации"
```

---

## 7. АНТИ-ПАТТЕРНЫ

```yaml
anti_patterns:
  - pattern: "Ручное редактирование content.js"
    why: "Будет перезаписано при следующей генерации"
    instead: "Редактировать WEBSITE_CONTENT.md"
    severity: CRITICAL
  
  - pattern: "Добавление фреймворков без необходимости"
    why: "Усложнение без выгоды"
    instead: "Vanilla JS для простых задач"
    severity: HIGH
  
  - pattern: "Маркетинговые штампы в тексте"
    why: "Противоречит tone of voice"
    instead: "Конкретные детали и атмосфера"
    severity: MEDIUM
  
  - pattern: "Перегруженный дизайн"
    why: "Противоречит минимализму"
    instead: "Больше воздуха, меньше элементов"
    severity: MEDIUM
  
  - pattern: "Коммит без тестирования"
    why: "Риск поломки продакшена"
    instead: "Всегда запускать build.py и тесты"
    severity: HIGH
  
  - pattern: "Деплой в main без проверки формы"
    why: "Риск потери конверсий"
    instead: "Обязательная проверка по FORM_CHECK_PROCEDURE.md"
    severity: CRITICAL
```

---

## 8. МЕТРИКИ УСПЕХА

```yaml
success_metrics:
  technical:
    build_validation: "100% тестов проходит"
    deployment: "Автоматический деплой без ошибок"
    page_load: "Быстрая загрузка без тяжелых ресурсов"
  
  ux:
    responsive: "Корректное отображение на всех устройствах"
    accessibility: "Читаемость, контрастность, семантика"
    language_switch: "Плавное переключение RU/AR"
  
  content:
    tone_consistency: "Единый tone of voice"
    completeness: "Вся информация для принятия решения"
    engagement: "Атмосферность, не сухость"
  
  conversion:
    form_operational: "Форма работает 100% времени"
    fallback_ready: "Резервный endpoint настроен"
    user_feedback: "Нет жалоб на broken form"
```

---

## 9. ЭВОЛЮЦИЯ ПРОЕКТА

```yaml
evolution_log:
  major_iterations:
    - phase: v1-100
      focus: "Базовая архитектура и контент"
      achievements:
        - Одностраничник
        - Build system
        - Контентная стратегия
    
    - phase: v101-150
      focus: "Дизайн-полировка и UX"
      achievements:
        - Типографическая система
        - Responsive design
        - Форма букинга
    
    - phase: v151-179
      focus: "Детальная доводка и билингвальность"
      achievements:
        - RU/AR переключение
        - Финальные правки дизайна
        - Скрытие version badge
    
    - phase: handshake-v3-v4
      focus: "AI-агентная синхронизация (Gemini ↔ Claude)"
      date: "28 октября 2025"
      achievements:
        - Исправлена ошибка E-1027 (День II, Vallois)
        - Добавлен Alvar Aalto (День IV)
        - Усилен вечер → "Разговор: синтез и итоги"
        - Обновлено био Натальи Логиновой
        - Добавлена ghost point 217 Faubourg (Jean Désert)
        - Создана FORM_CHECK_PROCEDURE.md
        - Валидирован протокол Gemini ↔ Claude
  
  current_version: handshake-v4
  git_commit_main: 2c213c9
  status: production
```

---

# II. ОПЕРАЦИОННЫЙ УРОВЕНЬ: РЕАЛИЗАЦИЯ

## 10. СТРУКТУРА ФАЙЛОВ

```yaml
file_structure:
  source_files:
    WEBSITE_CONTENT.md: "Основной контент на русском (source of truth)"
    WEBSITE_CONTENT_AR.md: "Контент на арабском (source of truth)"
    style.css: "Все стили проекта"
    index.html: "HTML структура + inline JS"
    build.py: "Генератор content.js из markdown"
    test_build.py: "Тестовый набор для валидации"
  
  generated_files:
    content.js: "Автогенерированный JS объект (НЕ РЕДАКТИРОВАТЬ)"
  
  documentation:
    PROJECT_KNOWLEDGE.md: "v2.1 - единый источник знаний (этот файл)"
    AI_COMMUNICATION_LOG.md: "История взаимодействий и решений"
    TO_GEMINI.md: "Инструкции для AI-ассистентов"
    FORM_CHECK_PROCEDURE.md: "Критическая процедура проверки формы"
    HANDSHAKE_V3_RESPONSE.md: "Протокол синхронизации Gemini↔Claude V3"
    HANDSHAKE_V4_RESPONSE.md: "Протокол синхронизации Gemini↔Claude V4"
  
  git:
    pre-commit: "Валидация перед коммитом"
```

---

## 11. ТЕХНИЧЕСКИЕ ПАТТЕРНЫ

```yaml
technical_patterns:
  content_generation:
    pattern: "Markdown → Python parser → JavaScript object"
    rationale: "Человекочитаемый source of truth"
    implementation: "build.py с YAML frontmatter парсингом"
  
  state_management:
    pattern: "Vanilla JS без фреймворков"
    storage: "localStorage для языка и предпочтений"
    rationale: "Простота, нет зависимостей"
  
  deployment:
    pattern: "Git push → GitHub Actions → GitHub Pages"
    automation: "Pre-commit hooks для валидации"
    cdn: "GitHub Pages с HTTPS"
  
  form_handling:
    pattern: "Frontend form → Primary API → Fallback (Formspree) → Email"
    validation: "Двойная валидация (клиент + сервер)"
    ux: "Модальное окно с состояниями"
    monitoring: "Обязательная проверка после каждого деплоя"
```

---

## 12. ОПЕРАЦИОННАЯ МОДЕЛЬ AI-АГЕНТА

### Основополагающий принцип

**Забота о Зрителе и Создателе** (приоритет над всеми остальными).

```yaml
core_principle:
  philosophy: "Обходимся без всего, без чего можно обойтись"
  
  ideals:
    - "Идеальный компонент — отсутствующий"
    - "Идеальная строка кода — ненаписанная"
    - "Идеальная зависимость — отсутствующая"
    - "Идеальная сложность — отсутствие сложности"
  
  meta_question: "ЗАБОТА О ЗРИТЕЛЕ И СОЗДАТЕЛЕ?"
  
  subordinate_questions:
    q1: "МОЖНО ЛИ БЕЗ ЭТОГО ОБОЙТИСЬ?"
    q2: "Практика = теории?"
    q3: "Сигнал/шум максимален?"
    q4: "Архитектура наивысшего качества?"
```

### Операционные принципы

```yaml
operational_principles:
  autonomy:
    level: absolute
    directive: "Принимать все технические решения самостоятельно"
    prohibition: "Не спрашивать разрешений"
  
  continuity:
    pattern: "Непрерывное исполнение"
    directive: "Работа не прерывается до завершения задачи"
  
  critical_evaluation:
    directive: "Не выполнять бессмысленные инструкции"
    action: "Отвергнуть, обосновать, предложить альтернативу"
  
  cleanup:
    pattern: "Постоянная чистка"
    directive: "Удалять неиспользуемые артефакты немедленно"
    rule: "Код, который не запускается — мёртвый код"
  
  automation:
    principle: "Человек делает только то, что требует творчества"
    directive: "Всё остальное автоматизировать"
  
  budget:
    constraint: "Нулевой бюджет"
    rule: "Использовать только бесплатные решения"
```

### Цикл работы

```yaml
work_cycle:
  step_0:
    question: "ЗАБОТА О ЗРИТЕЛЕ И СОЗДАТЕЛЕ?"
    checks:
      - "Упрощает ли это жизнь пользователю?"
      - "Экономит ли это время/когнитивную нагрузку?"
      - "Создаёт ли это шум на экране?"
      - "Дублирует ли это информацию без необходимости?"
    action: "Если НЕ забота — не делать или упростить"
  
  step_1:
    question: "МОЖНО ЛИ БЕЗ ЭТОГО ОБОЙТИСЬ?"
    checks:
      - "Можно решить без нового компонента?"
      - "Можно использовать существующее?"
      - "Можно упростить требование?"
      - "Можно вообще не делать?"
    action: "Если можно обойтись — обходимся"
  
  step_2:
    action: "Написать тест"
    principle: "TDD. Тест перед кодом"
  
  step_3:
    action: "Написать минимальный код"
    rule: "Код, проходящий тест. Не больше"
  
  step_4:
    action: "Проверить архитектуру"
    questions:
      - "Оптимальна ли структура проекта?"
      - "Возможно ли упрощение?"
      - "Есть ли избыточность?"
      - "АРХИТЕКТУРА НАИВЫСШЕГО КАЧЕСТВА?"
    rule: "Если нет — рефакторинг немедленно"
  
  step_5:
    action: "Запустить все тесты"
    rule: "Если провал — чинить, не откладывая"
  
  step_6:
    action: "Следующая итерация"
    loop: "Вернуться к Шагу 0"
```

### Стандарты коммуникации

```yaml
communication_standards:
  style:
    - "Директивы, не просьбы"
    - "Факты, не мнения"
    - "Действия, не намерения"
  
  prohibited_phrases:
    - "I hope this helps"
    - "Would you like"
    - "Let me know"
  
  anti_ai_patterns:
    prohibited:
      - "Вертикальные списки с жирными заголовками"
      - "Чекмарки (✓✗) в списках"
      - "Промо-язык: vibrant, rich tapestry, groundbreaking"
      - "Дидактизм: it's important to note"
      - "Резюме: In summary, In conclusion, Overall"
      - "Отрицательные параллелизмы: not only... but..."
      - "Title Case В Заголовках"
      - "Избыточные em-дaши (—)"
    
    goal: "Текст неотличим от человеческого письма"
```

---

## 13. ПОВТОРЯЮЩИЕСЯ ЗАДАЧИ

```yaml
recurring_tasks:
  - task: "Изменение текстового контента"
    steps:
      - "Редактировать WEBSITE_CONTENT.md"
      - "python3 build.py"
      - "git add, commit, push"
  
  - task: "Изменение стилей"
    steps:
      - "Редактировать style.css"
      - "Проверить на всех breakpoints"
      - "git add, commit, push"
  
  - task: "Добавление нового языка"
    steps:
      - "Создать WEBSITE_CONTENT_{LANG}.md"
      - "Обновить build.py для парсинга"
      - "Добавить переключатель в UI"
      - "Тестирование RTL/LTR"
  
  - task: "Реакция на фидбек пользователя"
    steps:
      - "Понять суть правки"
      - "Имплементировать изменение"
      - "Коммит с понятным сообщением"
      - "Деплой (автоматический)"
  
  - task: "Деплой в production (main)"
    steps:
      - "Запустить build.py и все тесты"
      - "git push origin main"
      - "Ждать 60 секунд (CDN propagation)"
      - "Проверить форму вручную (FORM_CHECK_PROCEDURE.md)"
      - "Если форма не работает → Emergency rollback"
    criticality: HIGH
```

---

# III. ДОМЕН: АР-ДЕКО И КУРАТОРЫ

## 14. ЗНАНИЕ О АР-ДЕКО

```yaml
art_deco:
  period: "1920-1939"
  
  characteristics:
    - геометрические формы
    - роскошные материалы
    - симметрия
    - модернистская элегантность
  
  key_figures:
    - name: "Jean-Louis Deniot"
      style: "Нео-деко, мужской ар-деко"
      signature: "Острая геометрия, контраст фактур"
      concept: "Атмосфера"
    
    - name: "Eileen Gray"
      style: "Модернизм через эргономику"
      signature: "Наблюдение за поведением человека"
      concept: "Забота (адаптация)"
    
    - name: "Alvar Aalto"
      style: "Органический модернизм"
      signature: "Эргономика как забота"
      concept: "Забота (человечность)"
    
    - name: "Jacques-Émile Ruhlmann"
      style: "Роскошное ар-деко"
      signature: "Дорогие материалы, мастерство"
      concept: "Демонстрация"
    
    - name: "Christian Liaigre"
      style: "Современный минимализм с ар-деко корнями"
      signature: "Лаконичность, благородные материалы"
      concept: "Демонстрация (современная)"
  
  paris_context: "Париж — эпицентр движения ар-деко"
  
  centenary: "2025 = 100 лет с Exposition 1925"
```

### Философия ар-деко (из транскриптов)

> **Ольга Розет (Recording 14):**  
> "Принципы ар-деко: не просто предметы, а ПРИНЦИПЫ. Большие пространства. Декоративный уровень отделки. Отобранные предметы с мастерством. Обязательно дорогие материалы. Винтаж и антиквариат как база."

---

## 15. КУРАТОРЫ ПРОГРАММЫ

### Ольга Розет

```yaml
olga_rozet:
  experience: "30+ лет в дизайне интерьеров"
  
  status: "Художник"
  
  instagram_profile:
    handle: "@olga.rozet"
    posts: 955
    followers: 8419
    following: 2006
    website_link: "parisinjanuary.ru"
    updated: "2025-10-29"
  
  education:
    - "Декоративно-прикладное искусство (МПГУ)"
    - "Дизайн интерьеров (Стаффордширский университет)"
    - "Искусствоведение (МГХПА им. Строганова, в процессе)"
  
  current_positions:
    - "Преподаватель ВБШД с 1995 года (30 лет)"
    - "Директор Творческой мастерской Ольги Розет"
    - "Куратор авторских путешествий с 2008 года"
  
  membership:
    - "IIDA (Международная ассоциация дизайнеров)"
    - "Британский институт дизайна"
  
  awards:
    - "Медаль «Профессионал России»"
  
  specialization:
    - "Ресторанные проекты (DKT hospitality)"
    - "Исторические интерьеры (ресторан Ц.Д.Л.)"
    - "Общественные пространства"
  
  expertise_in_program:
    focus: "Секреты мастеров: фактуры, цвет, индивидуальный почерк"
    philosophy: "То, что не видно в публикациях"
```

### Наталья Логинова

```yaml
natalia_loginova:
  background:
    - "Журналист ТК «Культура»"
    - "Главный редактор «Московское наследие»"
    - "Экс-руководитель Центра моды и дизайна Музея декоративного искусства"
  
  current_status:
    location: "Иммигрировала в Париж"
    reason: "Любовь к городу"
    activity: "Авторские туры по дизайну и архитектуре"
  
  expertise:
    - "Секретные крыши Парижа"
    - "Витражи"
    - "Детали архитектуры"
    - "Неочевидные места"
    - "«Париж через призму дизайна»"
  
  role_in_program:
    - "Локальная навигация (резидент Парижа)"
    - "Выбор музея для Дня I"
    - "Связь с владелицей Galerie Vallois"
    - "Маршрут выставки 1937"
  
  bio_current:
    - "Работает гидом по теме «Париж через призму дизайна»"
    - "Экс-руководитель Центра моды и дизайна Музея декоративного искусства, инициатор и соавтор проекта «Придумано и сделано в России»"
    - "Ведёт авторские профессиональные путешествия по Парижу для дизайнеров и архитекторов"
```

---

## 16. ЦЕЛЕВАЯ АУДИТОРИЯ

```yaml
target_audience:
  profile: "Взыскательные ценители искусства и дизайна"
  
  demographics:
    age: "30-55 лет"
    income: "Upper-middle class и выше"
    profession:
      - "Дизайнеры интерьера"
      - "Архитекторы"
      - "Декораторы"
      - "Art enthusiasts"
  
  values:
    - аутентичность
    - экспертность
    - качество
    - камерность
  
  pain_points:
    - "Массовые туры"
    - "Поверхностность"
    - "Туристические клише"
  
  desires:
    - "Глубокое погружение"
    - "Экспертный взгляд"
    - "Атмосфера"
    - "Индивидуальный подход"
  
  psychographics:
    - "Ценят образование и экспертизу"
    - "Путешествуют для inspiration, не relaxation"
    - "Готовы платить за уникальный доступ"
    - "Активны в профессиональных сообществах"
```

---

# IV. ИСХОДНИКИ И ДЕТАЛИ

## 17. ПРОГРАММА ТУРА (ПОЛНАЯ)

### ДЕНЬ I • 15 января — Правый берег

**Printemps Haussmann**
- Купол 1923 (Эжен Бриер): 20м диаметр, 3185 витражных панелей
- Металл: Эдгар Брандт (кованое железо)
- Студия Primavera (Ар-Деко мебель)
- Expo 1925

**Nolinski Paris (Жан-Луи Денье)**
- Материалы: Каррара, Nero Marquina, полированная латунь
- Стиль: "Мужской ар-деко", острая геометрия
- Концепция: Нео-деко, контраст фактур

**Legré**
- Робер Легре (décorateur-ensemblier, 1920-30-е)
- Материалы: палисандр, слоновая кость, лак
- Стиль: "Пышное ар-деко"

**Музей**
- Musée des Arts Décoratifs (MAD)
- Выставка "100 лет ар-деко" (октябрь 2025 — апрель 2026)
- Постоянная коллекция: Дюнан, Шаро

**217, rue du Faubourg Saint-Honoré** (GHOST POINT, добавлена 28.10.2025)
- Контекстуальная точка: фасад бывшей галереи "Jean Désert", которую Эйлин Грей открыла в 1922 году
- Rationale: Исторический якорь, специфичность, высокий signal/noise ratio (PK.md §25, q3)

---

### ДЕНЬ II • 16 января — Левый берег

**Saint-Germain-des-Prés**
- Rue de Seine — квартал антикваров с 1970-х
- Лак, хром, фанеровка

**Galerie Vallois (41 rue de Seine)**
- Робер Валлуа (открыта 1971)
- Эйлин Грей: кресло Fauteuil aux dragons (ЭКСПЕРТИЗА ГАЛЕРЕИ), кресло Transat, ширма Briques
- Рульманн, Дюнан, Пьер Шаро
- **ВАЖНО**: E-1027 удалена из описания (не специализация галереи, ошибка исправлена 28.10.2025)

**Palais de Tokyo + Trocadéro**
- Маршрут Expo 1937
- "Фея Электричества" Рауля Дюфи (250 панелей)

---

### ДЕНЬ III • 17 января — Maison & Objet

**Тема выставки:** "Past Reveals Future"

**Ключевые зоны:**
- What's New? In Decor (Elizabeth Leriche)
- Craft — Métiers d'Art (Павильон 5А)
- Signature (Павильон 7)
- Transformism by Harry Nuriev

**Фокус программы:**
- Тактильность, материалы
- Глянцевый лак + матовая керамика
- Архивные паттерны
- Авторский почерк

---

### ДЕНЬ IV • 18 января — Аалто

**Maison Louis Carré (1956-59)**
- Архитектор: Алвар Аалто
- Материалы: сосна, кожа, кирпич, медь
- Концепция: "Эргономика как забота"

**Детали:**
- Дверные ручки, обитые кожей
- Волнистый потолок
- Разноуровневые пространства

**Парк**
- Ландшафт и архитектура в ансамбле

**Вечер**
- **Разговор: синтез и итоги** (обновлено 28.10.2025, ранее просто "Разговор")

---

## 18. КОНТЕНТ САЙТА (WEBSITE_CONTENT.md)

```yaml
website_content:
  version: handshake-v4
  git_commit: 2c213c9
  deployment_date: 2025-10-28
  url: https://parisinjanuary.ru
  
  meta:
    title: "Индивидуальный почерк ар-деко. 100 лет — 4 дня в Париже (январь 2026)"
    description: "4 дня в Париже. Фактуры, материалы, атмосфера. Ольга Розет и Наталья Логинова."
    og_image: "https://parisinjanuary.ru/og-image.jpg"
```

### Ключевые изменения (Handshake V3/V4)

**1. День II / Galerie Vallois — Удаление E-1027:**

**БЫЛО:**
```
Эйлин Грей: столик E-1027, кресло Transat, ширма Briques
```

**СТАЛО:**
```
Эйлин Грей: кресло Fauteuil aux dragons, кресло Transat, ширма Briques
```

**Rationale**: E-1027 — не специализация галереи Vallois. Fauteuil aux dragons — экспертиза Vallois.

---

**2. День I / Маршрут — Добавление Ghost Point:**

**ДОБАВЛЕНО:**
```
**217, rue du Faubourg Saint-Honoré**

Контекстуальная точка: фасад бывшей галереи "Jean Désert", которую Эйлин Грей открыла в 1922 году
```

**Rationale**: Специфичность исторического якоря ("Jean Désert", 1922), высокий signal/noise ratio.

---

**3. День IV / Description — Добавление Alvar Aalto:**

**БЫЛО:**
```
### ЭРГОНОМИКА —<br>ЭТО ЗАБОТА

**<span class="red-accent">Поездка</span><br>в Maison Louis Carré**

Волна потолка...
```

**СТАЛО:**
```
### ЭРГОНОМИКА —<br>ЭТО ЗАБОТА

**<span class="red-accent">Поездка</span><br>в Maison Louis Carré**

<span class="architect-name">Alvar Aalto</span>

Волна потолка...
```

**Rationale**: Атрибуция архитектора, контекстная ясность.

---

**4. День IV / Вечер — Усиление CTA:**

**БЫЛО:**
```
**Вечер**

Разговор
```

**СТАЛО:**
```
**Вечер**

Разговор: синтез и итоги
```

**Rationale**: Более информативный заголовок, завершающая рамка программы.

---

**5. Кураторы / Наталья Логинова — Обновление биографии:**

**БЫЛО:**
```
• Журналист ТК «Культура»<br>
• Главный редактор «Московское наследие»<br>
• Иммигрировала в Париж, ведёт авторские туры
```

**СТАЛО:**
```
• Работает гидом по теме «Париж через призму дизайна»
• Экс-руководитель Центра моды и дизайна Музея декоративного искусства, инициатор и соавтор проекта «Придумано и сделано в России»
• Ведёт авторские профессиональные путешествия по Парижу для дизайнеров и архитекторов
```

**Rationale**: Ground Truth = Curator Feedback (CONTEXT_DATA 2.0, Screenshot 2025-10-28).

---

### Связанный артефакт: FORM_CHECK_PROCEDURE.md

**Создан**: 28 октября 2025  
**Git Commit**: 660c4d6  
**Статус**: Обязательная процедура

**Содержание:**
1. Автоматизированные проверки (bash script)
2. Мануальный чек-лист (пошаговая валидация)
3. Текущее состояние формы (V4 документация)
4. Emergency rollback процедура
5. Определение метрик успеха ("working" vs "broken")

**Policy**: Форма = критический элемент, проверка при КАЖДОМ деплое в `main`.

---

### Hero

```
Индивидуальный почерк ар-деко
100 лет • 

Фактуры, материалы, атмосфера.
Можно ли ощутить словами?
4 ДНЯ
с Ольгой Розет и Натальей Логиновой

15–18+ января 2026 | до 12 человек | 1 550 €
```

### Ключевая философия

```
Денье, Легре, Эйлин Грей, Аалто. 
У каждого свой почерк.

В интерьерах видны соотношения фактур, 
тонкости цвета, работа с материалами.

Необходим ли контакт с Реальностью?
```

---

## 19. ИСХОДНЫЕ МАТЕРИАЛЫ

```yaml
source_materials:
  audio_recordings:
    count: 7
    total_duration: "~2 часа"
    language: Русский
    participants: [Ольга Розет, Ася]
    
    recordings:
      - file: "New Recording 14.m4a"
        transcript: "New Recording 14.txt"
        duration: "~45 минут"
        key_topics:
          - "Структура программы"
          - "Философия секретов мастеров"
          - "Ценообразование (1550€)"
        status: "⭐ САМАЯ ВАЖНАЯ ЗАПИСЬ"
      
      - file: "New Recording 15.m4a"
        key_topics: [Deco Off, Palais de Tokyo, галереи]
      
      - file: "New Recording 16.m4a"
        key_topics: [Алвар Аалто, финский модернизм, Maison Carré]
      
      - file: "New Recording 18.m4a"
        key_topics: [Nolinski, Deniot, Эйлин Грей, винтаж]
      
      - file: "New Recording 20.m4a"
        key_topics: [Индивидуальный почерк, Мельников 1925]
      
      - file: "New Recording 21.m4a"
        key_topics: [Редактура лендинга, формулировки]
      
      - file: "New Recording 22.m4a"
        key_topics: [Финальные правки, метафоры]
  
  screenshots:
    previus_landing: 11 файлов
    date: "16 октября 2025"
  
  documents:
    - "Programme - Maison&Objet.pdf (4.4 MB)"
    - "shorthand (краткий конспект)"
```

---

## 20. КЛЮЧЕВЫЕ ЦИТАТЫ (ПРОВЕРЕНО)

### Секреты мастеров
> "Мы будем в интерьерах смотреть секреты мастеров. Соотношения фактуры текстур, тонкости цвета, которые не видны ни в одной публикации."  
> — Ольга Розет, Recording 14

### Почерк мастера
> "Почерк мастера, сигначи"  
> — Ольга Розет, Recording 14

### Эргономика как забота
> "Аргономика как забота"  
> — Ольга Розет, Recording 21

### Заботливая эстетика
> "Заботливая эстетика, она может в разном проявляться"  
> — Ольга Розет, Recording 21

### Наблюдение за человеком
> "Через наблюдение за поведением"  
> — Ольга Розет, Recording 21

### Глубина материалов
> "По цветам глубокие, по материалам глубокие"  
> — Ольга Розет, Recording 22

### Неживой интерьер
> "Парижские дизайнеры смешивают новое со старым. Интерьер без предметов с историей выглядит неживо."  
> — Ольга Розет, Recording 22

---

## 21. ПРЕДЫДУЩАЯ КАМПАНИЯ (SEPTEMBER 2025)

```yaml
paris_september_2025:
  dates: "4–8 сентября 2025"
  status: "Успешно проведена"
  
  visual_concept:
    motif: "Керамические объекты"
    philosophy: "Минимализм + символизм"
    colors:
      - терракотовый красный
      - яркий синий
      - off-white
  
  key_materials:
    - campaign_consolidated_brief_v1.txt
    - campaign_technical_brief_v1.txt
    - Landing Text Integration.txt
    - IG Post.txt
    - 100+ керамических PNG
  
  lessons_learned:
    works:
      - "Керамические визуалы = уникальная идентичность"
      - "Детальные био кураторов повышают доверие"
      - "Telegram-чат укрепляет комьюнити"
    
    to_improve:
      - "Более чёткие условия отмены/возврата"
      - "Раннее бронирование со скидкой"
      - "Больше видео-контента"
  
  continuity_with_january:
    preserve:
      - Визуальный язык (керамика)
      - Структура лендинга
      - Тон коммуникации
      - Фокус на экспертизе
    
    adapt:
      - Даты (январь вместо сентября)
      - Программа (ар-деко вместо Design Week)
      - Локации (Deniot, Legré, Aalto)
```

---

## 22. ДИАЛОГИ С GEMINI (КАМПАНИЯ)

```yaml
gemini_strategy_insights:
  platform: gemini.google.com
  period: "Сентябрь–октябрь 2025"
  
  key_recommendations:
    organic_reach:
      principle: "Instagram как диалог, не трансляция"
      priority_formats: [Reels, Карусели, Stories, Guides]
      engagement_threshold: ">3% = отлично"
    
    branding:
      recommendation: "Единый бренд с сезонными расширениями"
      example: "Paris Design Tours by [Curator] — January Edition"
    
    visual_aesthetics:
      color: "Deep jewel tones (emerald, sapphire, gold) + black/white"
      typography: "Geometric sans-serif + elegant serif"
      photography: "High contrast, dramatic shadows, architectural angles"
    
    conversion_funnel:
      stage_1: "Awareness (Reels, хэштеги)"
      stage_2: "Interest (Educational content)"
      stage_3: "Consideration (Отзывы, FAQ)"
      stage_4: "Conversion (CTA, scarcity)"
      stage_5: "Advocacy (UGC, скидка на следующий тур)"
    
    metrics_that_matter:
      - Engagement rate
      - Saves
      - Shares
      - DM
      - Link clicks
      - Conversion rate
  
  philosophy:
    quote: "You're not selling a tour. You're offering access to a world that's usually closed."
```

---

## 23. MAISON & OBJET ДЕТАЛИ

```yaml
maison_objet_2026:
  dates: "15–19 января 2026"
  location: "Paris Nord Villepinte"
  theme: "PAST REVEALS FUTURE"
  
  scale:
    brands: 2300
    new_brands: 500
    sectors: 6
    halls: 7
    conferences: 25
  
  relevant_exhibitions:
    - name: "What's New? In Decor"
      curator: "Elizabeth Leriche"
      focus: "Тактильность, материалы, архивные паттерны"
      relevance: "⭐⭐⭐⭐⭐ ЭПИЦЕНТР ДЛЯ ГРУППЫ"
    
    - name: "Craft — Métiers d'Art"
      location: "Павильон 5А"
      focus: "Маркетри, эмаль, стекло, след резца"
      relevance: "⭐⭐⭐⭐⭐ ПРЯМОЙ ОТВЕТ НА ПОЧЕРК"
    
    - name: "Signature"
      location: "Павильон 7"
      focus: "Авторский стиль, латунь (полированная/патинированная)"
      relevance: "⭐⭐⭐⭐ СЕКТОР ИМЕН"
    
    - name: "Transformism by Harry Nuriev"
      location: "Hall 3"
      role: "Designer of the Year 2026"
      relevance: "⭐⭐⭐ РАДИКАЛЬНЫЙ ЦВЕТ"
  
  strategy_for_group:
    ignore:
      - "Generic павильоны (Today, Home Accessories)"
    
    focus:
      - "Signature (Павильон 7)"
      - "Craft (Павильон 5А)"
    
    approach:
      - "Смотреть не на предмет, а на узел соединения"
      - "Искать авторский след (ручная неровность)"
      - "Сравнивать интерпретации (3-4 стенда с одним материалом)"
```

---

# V. INSTAGRAM КАМПАНИЯ (ОКТЯБРЬ 2025)

## 26. INSTAGRAM CAMPAIGN EXECUTION

### 26.1 IG Font Analysis Summary

**Контекст**: Технический анализ нативных шрифтов Instagram Stories для оценки workflow.

**Среда рендеринга**:
- Instagram использует **системные шрифты** (не встроенные):
  - iOS: San Francisco
  - Android: Roboto
- Макеты из Affinity/Figma не будут 100% pixel-perfect

**Анализ шрифтов (кириллица)**:

```yaml
основные_шрифты_ok:
  - Modern: "SF/Roboto, чёткость, высокая читаемость"
  - Classic: "Times New Roman, serif, универсальная кириллица"
  - Typewriter: "Courier, моноширинный, ностальгия"

проблемные_шрифты:
  - Strong: "Forced justification, рваные строки"
  - Neon: "Glow effect, потеря чёткости в малом кегле"

дисплейные_риски:
  - Elegant/Literature: "Близок к Cormorant, но рендеринг нестабилен"
  - Новые: "Deco, Poster — часто без кириллицы или неполная поддержка"

ui_элемент_unavailable:
  - Instagram Sans Condensed Bold: "Стикер 'Ссылка', недоступен для набора текста"
```

**"Стратегия Изоляции"** (анализ workflow):

```yaml
strategy_isolation:
  concept: "Не использовать нативные шрифты ИГ для верстки текста, если нужен 100% контроль"
  
  process:
    - "1. Верстка в Affinity Designer (или Figma)"
    - "2. Экспорт PNG (текст 'запечен' в изображение)"
    - "3. Загрузка в Instagram Stories"
    - "4. Добавление ТОЛЬКО стикера 'Ссылка' в ИГ"
  
  pros:
    - "Полный контроль над типографикой"
    - "Точное воспроизведение дизайн-системы"
    - "Независимость от платформы"
  
  cons:
    - "Текст неинтерактивен (не копируется, не переводится)"
    - "Шрифт стикера отличается от основного текста"
    - "Дополнительный шаг в workflow"
```

**Выводы**:
- Для сложной типографики (Cormorant, Forum) → "Стратегия Изоляции" оптимальна
- Для простых объявлений → нативный Modern/Classic достаточен
- Стикер "Ссылка" = единственный допустимый UI-элемент ИГ в дизайне

---

### 26.2 Final IG Font Decision (TASK V22)

**Контекст**: Учитывая IG_FONT_ANALYSIS.md, принцип q0 "Забота о Зрителе и Создателе" и цель минимизации шума на экране CTA.

**Решение**: Для данной кампании используется **гибридный подход**.

```yaml
final_font_decision:
  method: "Hybrid (текст в макете + нативный стикер)"
  
  implementation:
    stories_1_2_3:
      text_method: "Запечен в PNG (Стратегия Изоляции)"
      font: "Cormorant Garamond / Forum (из дизайн-системы)"
      cta_sticker: "Нативный стикер 'Ссылка' (Instagram Sans)"
  
  rationale:
    - "Сохранение визуальной целостности с landing page"
    - "100% контроль над типографикой (фирменный стиль)"
    - "Минимизация количества шрифтов (Cormorant/Forum + Стикер)"
    - "Забота о Создателе: простейший workflow (экспорт PNG)"
  
  trade_off:
    accepted: "Стикер 'Ссылка' имеет другой шрифт (Instagram Sans), но это UX-стандарт платформы"
    acceptable: "Пользователи привыкли к стикеру, распознают его как CTA"
```

**Примечание**: Хотя анализ указывал на возможность использования нативного Modern для всего текста, финальное решение отдало предпочтение "Стратегии Изоляции" для сохранения фирменного стиля.

---

### 26.3 Published Stories (Oct 28)

**Workflow**: "Стратегия Изоляции" (текст "запечен" в PNG, шрифты Cormorant/Forum).

**Публикация**: 28 октября 2025  
**Формат**: Триптих (3 сториз)  
**Файлы**: `s1.png`, `s2.png`, `s3.png`

---

#### Story 1: Hook (Захват внимания)

**Визуал**:
```yaml
visual_story_1:
  background: "#0A2342 (midnight blue)"
  imagery: "Ар-Деко глаз (золото, бриллианты)"
  composition: "Центральная фокусировка, симметрия"
  style: "Роскошь, геометрия, демонстрация"
```

**Текст (полный)**:
```
ИНДИВИДУАЛЬНЫЙ ПОЧЕРК АР-ДЕКО

+

ЧЕЛОВЕЧНОСТЬ
В ПОДХОДЕ И МАТЕРИАЛЕ
```

**Narrative axis**: Введение оси "**Человечность**" (от индивидуального почерка к человечности).

**Цель**: Остановить скролл эмоциональным визуалом + философским заголовком.

---

#### Story 2: Value (Ценностное предложение)

**Визуал**:
```yaml
visual_story_2:
  background: "#F8F6F3 (warm white)"
  imagery: "Рука Аалто (деревянная ручка двери)"
  composition: "Детальный крупный план, тактильность"
  style: "Тепло, органичность, забота"
```

**Текст (полный)**:
```
ЧЕЛОВЕЧНОСТЬ МОДЕРНИЗМА:

+

ЭРГОНОМИКА — ЭТО ЗАБОТА.
```

**Narrative axis**: Развитие оси "Человечность" → конкретизация через Аалто.

**Цель**: Показать философию через визуал + короткую формулировку.

---

#### Story 3: CTA (Призыв к действию)

**Визуал**:
```yaml
visual_story_3:
  background: "#E31B1B (accent red)"
  imagery: "Геометрический паттерн Ар-Деко внизу"
  composition: "Текстовая доминанта, паттерн как якорь"
  style: "Энергия, действие, решительность"
```

**Текст (полный)**:
```
В ПАРИЖЕ

+

15–18+
ЯНВАРЯ 2026

+

ЕСЛИ НЕТ ВИЗЫ —
ПОДАВАЙТЕ ДОКУМЕНТЫ СЕЙЧАС.
```

**Functionality**:
- Стикер "Ссылка": `https://parisinjanuary.ru`
- Текст стикера: "Программа и бронирование"

**Link Clicks**: 11 (CTR ~6.2% от 177 достигнутых) — **высокий показатель**.

**Цель**: Конкретная информация (даты) + urgency (виза) + прямая ссылка.

---

### 26.4 Published Post (Oct 28)

**Формат**: Карусель (1 изображение) + длинный caption  
**Файл**: `IMG_4715.jpg - IMG_4718.png` (замочная скважина Ар-Деко)

---

**Визуал (детальное описание)**:
```yaml
visual_post:
  subject: "Замочная скважина Ар-Деко"
  materials: "Дерево (тёмное, полированное) + металл (латунь/бронза, патина)"
  composition: "Центральная ось, симметрия, геометрический паттерн"
  style: "Тактильность, ремесло, детализация"
  framing: "Крупный план, фокус на фактуре и мастерстве"
```

**Фрейминг поста**:
```
ЖИВОЕ ИССЛЕДОВАНИЕ В ПАРИЖЕ
```

---

**Текст поста (полный)**:
```
15–18+ ЯНВАРЯ
2026

ЖИВОЕ ИССЛЕДОВАНИЕ

В ПАРИЖЕ

с Ольгой Розет
и Натальей Логиновой:

Индивидуальный почерк ар-деко:
100 лет,

включая
Maison et Objet.

•

Физический контакт.
Фактуры. Материалы. Атмосфера.

Наблюдаем ремесло.

•

Связываем коннотации материалов:
Демонстрация
Рульманна и Легре;
Атмосфера
Денье;
Забота
Грей и Аалто.

•

Эргономика.
Функция.
Украшение.

•

Группа до 12 человек.

•

Подробнее:
parisinjanuary.ru

•

Виза делается долго.
Нет визы —
подавайте на визу сейчас.
```

---

**Философия (каноническая интерпретация)**:

```yaml
canonical_figure_concept_mapping:
  demonstration: 
    figures: [Ruhmann, Liaigre]
    concept: "Материал как статус, мастерство как демонстрация"
  
  atmosphere:
    figure: Deniot
    concept: "Материал как настроение, нео-деко элегантность"
  
  care:
    figures: [Eileen Gray, Alvar Aalto]
    concept: "Эргономика как забота, человечность модернизма"
```

**Ключевые слова** (из текста поста):
- Физический контакт
- Фактуры, материалы, атмосфера
- Наблюдаем ремесло
- Эргономика, функция, украшение

---

**CTA / Логистика**:
- Даты: 15–18+ ЯНВАРЯ 2026
- Группа: до 12 человек
- Сайт: parisinjanuary.ru
- Urgency: "Виза делается долго. Нет визы — подавайте на визу сейчас"

---

**Хэштеги (полный список)**:
```
#ArtDeco
#Craft
#ParisArtDeco
#Ruhlmann
#EileenGray
#AlvarAalto
#ParisDesign
#FrenchDesign
#MaisonObjet
#MaisonObjet2026
#ОльгаРозет
#НатальяЛогинова
#ФранцузскийДизайн
#ДизайнОбразование
#Париж
#ДизайнПутешествие
```

---

### 26.5 IG Insights Summary (Oct 29)

**Источник**: `IG Insights 29 Oct 2025.txt`

---

#### Post "Замочная скважина" (28 Oct)

```yaml
post_performance:
  views: 730
  reach:
    total: 357
    followers: 83.4%
    non_followers: 16.6%
  
  engagement:
    total_interactions: 16
    likes: 16
    comments: 0
    saves: 0
    shares: 0
    engagement_rate: 4.5% (16/357)
  
  traffic_sources:
    from_home: 379
    from_other: 286
    from_profile: 65
  
  profile_activity:
    profile_visits: 0
    link_taps: 0
```

**Вывод**: Низкая вовлеченность (только Likes, нет Saves/Shares), но достойный reach для органики.

---

#### Stories (Триптих, 28 Oct)

**Story 1 (Hook — синий фон, глаз)**:
```yaml
story_1_performance:
  views: 247
  reach: 190
  followers_percent: 97.2%
  
  engagement:
    total_interactions: 4
    likes: 4
    shares: 0
    replies: 0
  
  navigation:
    forwards: 185 (74.9%)
    back: 22
    exited: 10
    next_story: 6
```

**Вывод**: Высокий forward rate (74.9%) — быстрый переход к Story 2.

---

**Story 2 (Value — белый фон, рука Аалто)**:
```yaml
story_2_performance:
  views: 214
  reach: 180
  followers_percent: 100%
  
  engagement:
    total_interactions: 6
    likes: 6
    shares: 0
    replies: 0
  
  navigation:
    forwards: 172 (80.4%)
    back: 18
    next_story: 7
    exited: 3
```

**Вывод**: Ещё выше forward rate (80.4%), удержание аудитории.

---

**Story 3 (CTA — красный фон, CTA)**:
```yaml
story_3_performance:
  views: 234
  reach: 177
  followers_percent: 99.1%
  
  engagement:
    total_interactions: 9
    likes: 9
    shares: 0
    replies: 0
  
  link_clicks: 11 (CTR: 6.2% от reach)
  
  navigation:
    forwards: 160 (68.4%)
    back: 8
    exited: 22 (9.4%)
    next_story: 10
```

**Вывод**: **Высокий CTR ~6.2%** (11 кликов из 177 reach) — отличный показатель для organic Stories. Рост Exited (9.4%) нормален для финальной сториз.

---

#### Общие паттерны (90 дней, аккаунт Ольги)

```yaml
top_content_by_views_90d:
  - views: 3900
    date: "23 Aug"
    type: "Личный контент (фото Ольги)"
  
  - views: 3300
    date: "28 Sep"
    type: "Reels"
  
  - views: 2600
    date: "24 Sep"
    type: "Reels"

top_content_by_engagement_90d:
  - interactions: 199
    date: "28 Sep"
    type: "Reels (личный контент)"
  
  - interactions: 175
    date: "24 Sep"
    type: "Reels (личный контент)"

audience_activity_peak:
  days: [Вт, Ср, Чт]
  time: "18:00-21:00"
  follower_concentration: [Вт: 1334, Чт: 1449]
```

**Вывод**: 
- **Личный контент** (фото Ольги) >> анонсы
- **Reels** >> статичные посты
- Оптимальное время публикации: **Вт-Чт, 18:00-21:00**

**Рекомендация**: Интеграция личного контента (за кулисами, подготовка) + Reels для усиления охвата анонсов.

---

### 26.6 IG Promotion Guide Summary

**Источник**: "Простой гид по продвижению в Instagram (2025)"  
**Дата анализа**: 29 октября 2025

**Основной принцип**: Два типа контента для разных целей:

```yaml
content_types:
  retention:
    formats: [Stories, Карусели]
    goal: "Удержание существующих подписчиков"
    key_metric: "Лайки"
  
  growth:
    formats: [Reels]
    goal: "Привлечение новых подписчиков"
    key_metric: "Репосты"
```

---

#### Приоритеты алгоритма Instagram (2025)

```yaml
algorithm_priorities:
  priority_1: "Время просмотра (watch time)"
  priority_2: "Репосты (shares)"
  priority_3: "Сохранения (saves)"
  priority_4: "Лайки и комментарии"
```

**Вывод**: Алгоритм приоритизирует **удержание внимания** и **распространение** выше, чем простые взаимодействия.

---

#### Форматы контента

**Reels (Рост)**:
```yaml
reels_best_practices:
  hook: "Крючок в первые 0-2 секунды"
  looping: "Зацикленность (начало = конец)"
  duration: "< 3 минуты (идеально < 60 сек)"
  quality:
    - "Без вотермарок других платформ"
    - "С аудио (музыка/голос)"
    - "Оригинальный контент (не репост)"
  key_metric: "Репосты"
```

**Карусели (Польза)**:
```yaml
carousels_best_practices:
  first_slide: "Цепляющий визуал/заголовок"
  use_case: "Гайды, инструкции, пошаговые разборы"
  key_metric: "Сохранения"
```

**Stories (Общение)**:
```yaml
stories_best_practices:
  interactivity: "Использовать стикеры (опросы, вопросы, слайдеры)"
  goal: "Диалог с подписчиками"
  key_metric: "Replies, Shares"
```

---

#### Discovery (Как находят профиль)

**Поиск Instagram** (важнее хэштегов):

```yaml
search_optimization:
  priority_1: "Имя профиля (Name field, не username)"
  priority_2: "Био"
  priority_3: "Подписи к постам"
  priority_4: "Alt-текст изображений"
  
  keywords:
    rule: "Использовать ключевые слова в Имени, Био, Подписях"
    example_name: "Ольга Розет • Дизайн • Париж"
```

**Хэштеги** (вспомогательная роль):

```yaml
hashtags_best_practices:
  quantity: "3-5 узких, точных"
  purpose: "Помогают ИГ понять тему контента"
  avoid: "Широкие хэштеги (#art, #design) — бесполезны"
  prefer: "Узкие (#ParisArtDeco, #MaisonObjet2026)"
```

---

#### Профиль (3 секунды на решение о подписке)

```yaml
profile_optimization:
  закрепленные_посты: "Первое впечатление, лучшие работы"
  актуальное: "Highlights Stories (категории)"
  био: "Четкое ценностное предложение + ключевые слова"
  
  decision_time: "3 секунды"
  action: "Закрепить топ-3 поста, обновить Highlights"
```

---

#### Процесс продвижения

```yaml
promotion_workflow:
  step_1: "Анализ статистики (Insights)"
  step_2: "Усиление работающего (больше того, что приносит результат)"
  step_3: "Ведение дневника (фиксация паттернов)"
  step_4: "Эксперименты (новые форматы, темы)"
```

**Философия**: Не гадать, а **тестировать и масштабировать** успешное.

---

### 26.7 Refined IG Strategy (Gemini Vision, Task V25)

**Дата разработки**: 29 октября 2025  
**Основа**: `PK.md §26.5` (Insights), "Простой гид..." (Алгоритм 2025), каноническая связка Фигура—Концепция (`PK §26.4`)

---

#### Цель стратегии (Двухцелевая)

```yaml
strategic_goals:
  goal_1:
    name: "Удержание подписчиков Ольги"
    audience: "8,419 текущих подписчиков"
    approach: "Stories + Карусели (польза, общение)"
  
  goal_2:
    name: "Привлечение новых (потенциальные участники тура)"
    audience: "Дизайнеры, архитекторы, art enthusiasts (30-55 лет)"
    approach: "Reels (рост через репосты)"
```

---

#### Форматы контента (Микс ~40/40/20)

**Stories (40%, Удержание/Конверсия, Приоритет #1)**:

```yaml
stories_strategy:
  priority: "Приоритет #1 (высокий CTR 6.2%, PK §26.5)"
  
  themes:
    - "За кулисами" (подготовка к туру, локации)
    - "Мини-уроки" ("Секреты мастеров" — 15-30 сек)
    - "Опросы" (Какой формат интереснее? Кто был в Париже?)
    - "Q&A" (Ответы на вопросы о туре/визе/программе)
  
  interactivity:
    - "Использовать стикеры Опроса, Вопроса, Слайдера"
    - "Цель: диалог, не монолог"
  
  cta_strategy:
    placement: "Story 3 в серии (по модели Oct 28)"
    format: "Стикер 'Ссылка' → parisinjanuary.ru"
    urgency: "Виза делается долго — подавайте сейчас"
  
  frequency: "Ежедневно (1-3 сториз)"
  timing: "18:00-21:00 (пик активности, PK §26.5)"
```

**Обоснование**: Stories показали **CTR 6.2%** на CTA (`PK §26.5`) — лучший формат для конверсии. Алгоритм 2025 приоритизирует интерактивность.

---

**Reels (40%, Рост, Приоритет #1)**:

```yaml
reels_strategy:
  priority: "Приоритет #1 (топ по вовлеченности, PK §26.5)"
  
  themes:
    personal_content:
      description: "Личный контент Ольги (работает лучше всего)"
      examples:
        - "Ольга в мастерской (процесс работы)"
        - "Ольга показывает образцы материалов"
        - "Ольга рассказывает о любимом предмете ар-деко"
      rationale: "Топ контент за 90 дней = личный (PK §26.5)"
    
    visual_riddles:
      description: "Визуальные 'загадки' (угадай мастера по детали)"
      examples:
        - "Деталь мебели → Угадай: Рульманн или Легре?"
        - "Ручка двери → Чья работа?"
      rationale: "Удержание внимания (watch time)"
    
    atmospheric_cuts:
      description: "Атмосферные нарезки (визуал + музыка)"
      examples:
        - "Париж глазами дизайнера (музей, галереи, детали)"
        - "Maison & Objet: ремесло в движении"
      rationale: "Распространение (shares)"
  
  hook: "0-2 сек: вопрос/интрига/красивый кадр"
  duration: "< 60 секунд (идеально 30-45)"
  audio: "Использовать трендовое аудио (но не обязательно)"
  
  frequency: "2-3 в неделю"
  timing: "Вт-Чт, 18:00-21:00"
```

**Обоснование**: Reels с личным контентом Ольги = **топ по views (3.9K) и engagement (199)** за 90 дней (`PK §26.5`). "Гид" подтверждает: Reels = рост через репосты.

---

**Карусели (20%, Польза/Удержание, Приоритет #2)**:

```yaml
carousels_strategy:
  priority: "Приоритет #2 (для сохранений)"
  
  themes:
    figure_concept_breakdowns:
      description: "Разбор связки Фигура—Концепция (PK §26.4)"
      examples:
        - "Слайд 1: Рульманн. Слайд 2: Материал как демонстрация. Слайд 3: Где увидим"
        - "Серия: Денье → Атмосфера, Грей+Аалто → Забота"
      rationale: "Образовательная ценность = сохранения"
    
    guides:
      description: "Гайды в стиле '3 признака почерка Рульманна'"
      examples:
        - "5 деталей, выдающих мастера ар-деко"
        - "Как отличить Рульманна от Легре (визуально)"
      rationale: "Полезный контент = сохранения"
  
  first_slide: "Цепляющий заголовок + визуал"
  format: "5-7 слайдов (не перегружать)"
  
  frequency: "1-2 в неделю"
  timing: "Вт-Чт, 18:00-21:00"
```

**Обоснование**: Карусели = формат для **сохранений** ("Гид"). Связка Фигура—Концепция уже есть (`PK §26.4`) — использовать как базу.

---

#### Визуал (Сохранение идентичности)

```yaml
visual_strategy:
  approved_assets:
    - "Замочная скважина Ар-Деко (IMG_4715.jpg)"
    - "Глаз Ар-Деко (s1.png)"
    - "Рука Аалто (s2.png)"
    - "Геометрический паттерн (s3.png)"
  
  adaptation:
    - "Для Reels: использовать эти визуалы + движение (zoom, pan)"
    - "Для Карусель: адаптировать паттерны как фоны"
  
  design_system:
    palette: "PK §3 (Midnight Blue, Warm White, Accent Red)"
    fonts: "PK §3 (Cormorant, Inter, Forum)"
    philosophy: "Минимализм без холодности"
```

**Обоснование**: Утвержденные визуалы уже соответствуют дизайн-системе проекта (`PK §3`). Не создавать новое — адаптировать существующее.

---

#### Тексты (Принцип "Без избыточности")

```yaml
text_strategy:
  principle: "Без избыточности (PK §4)"
  
  rule: "Промо-текст ДОПОЛНЯЕТ сайт, не ДУБЛИРУЕТ"
  
  allowed_repetition:
    - "Якорные фразы" (15–18+ января, parisinjanuary.ru, 1550 €)
    - "Имена" (Ольга Розет, Наталья Логинова)
  
  avoid_repetition:
    - "Полное описание программы (есть на сайте)"
    - "Подробности включенного (есть на сайте)"
  
  use_figure_concept:
    - "Демонстрация → Рульманн/Легре"
    - "Атмосфера → Денье"
    - "Забота → Грей/Аалто"
```

**Обоснование**: Принцип q0 "Забота о Зрителе" (`PK §12`) = минимизация шума.

---

#### Discovery (Оптимизация поиска)

```yaml
discovery_strategy:
  profile_name_optimization:
    current: "Ольга Розет"
    recommended: "Ольга Розет • Дизайн интерьера • Париж"
    rationale: "Имя = приоритет #1 для поиска ИГ"
  
  bio_optimization:
    keywords: ["Дизайн интерьеров", "Ар-деко", "Париж", "Кураторские туры"]
    structure: "Художник | Дизайн интерьеров | Кураторские туры по Парижу"
  
  hashtags_refined:
    quantity: "3-5 узких"
    examples:
      - "#ParisArtDeco"
      - "#MaisonObjet2026"
      - "#ДизайнПутешествие"
      - "#AlvarAalto"
      - "#EileenGray"
    avoid: ["#Париж", "#ArtDeco" (слишком широкие)]
```

**Обоснование**: "Гид" указывает: поиск ИГ > хэштеги. Оптимизировать Имя и Био = приоритет.

---

#### Частота и время

```yaml
posting_schedule:
  frequency:
    stories: "Ежедневно (1-3 сториз)"
    reels: "2-3 раза в неделю"
    carousels: "1-2 раза в неделю"
    total: "3-4 основных поста в неделю + ежедневные Stories"
  
  timing:
    optimal_days: [Вт, Ср, Чт]
    optimal_time: "18:00-21:00"
    source: "PK §26.5 (Insights аккаунта Ольги)"
```

---

#### CTA (Call to Action)

```yaml
cta_strategy:
  primary_channel: "Stories (стикер 'Ссылка')"
  
  secondary_channel: "Мягкий CTA в постах/Reels ('Подробности → ссылка в профиле')"
  
  urgency_messaging:
    - "Виза делается долго"
    - "Нет визы — подавайте документы сейчас"
    - "Группа до 12 человек (ограниченность)"
  
  link_destination: "parisinjanuary.ru (прямая ссылка в профиле)"
```

---

#### Метрики успеха

```yaml
success_metrics:
  growth:
    primary: "Репосты (Reels)"
    secondary: "Новые подписчики (дизайнеры/архитекторы)"
  
  retention:
    primary: "Сохранения (Карусели)"
    secondary: "Replies/Shares (Stories)"
  
  conversion:
    primary: "Link Clicks (Stories)"
    secondary: "DM с вопросами о туре"
  
  targets:
    link_ctr: "> 5% (текущий 6.2%)"
    engagement_rate: "> 3%"
    shares_per_reel: "> 5"
```

---

### 26.8 Hashtag Analysis

**Контекст**: Анализ текущих хэштегов (пост Oct 28, `PK §26.4`) vs рекомендации "Простого гида..."

---

#### Текущие хэштеги (16 штук)

```yaml
current_hashtags:
  total: 16
  
  narrow_specific:
    - "#MaisonObjet2026"
    - "#AlvarAalto"
    - "#EileenGray"
    - "#Ruhlmann"
    - "#ОльгаРозет"
    - "#НатальяЛогинова"
  
  medium:
    - "#ParisArtDeco"
    - "#ParisDesign"
    - "#FrenchDesign"
    - "#ДизайнОбразование"
    - "#ДизайнПутешествие"
  
  broad_generic:
    - "#ArtDeco"
    - "#Craft"
    - "#MaisonObjet"
    - "#ФранцузскийДизайн"
    - "#Париж"
```

---

#### Рекомендация "Гида"

```yaml
guide_recommendation:
  quantity: "3-5 узких, точных"
  purpose: "Помочь ИГ понять тему (не для охвата)"
  avoid: "Широкие хэштеги (#ArtDeco, #Париж) — бесполезны"
```

---

#### Вывод и рекомендация для будущих постов

```yaml
analysis_conclusion:
  current_status: "Избыточно (16 хэштегов)"
  issue: "Смешаны узкие и широкие — снижает релевантность"
  
  recommended_set_v2:
    hashtags:
      - "#ParisArtDeco"
      - "#MaisonObjet2026"
      - "#ДизайнПутешествие"
      - "#EileenGray"
      - "#AlvarAalto"
    
    rationale:
      - "ParisArtDeco: узкая ниша (ар-деко + Париж)"
      - "MaisonObjet2026: событие (высокая релевантность)"
      - "ДизайнПутешествие: целевая аудитория"
      - "EileenGray/AlvarAalto: фигуры программы"
  
  action: "Использовать 3-5 из рекомендованного набора для будущих постов"
```

---

**Примечание**: Текущий пост (Oct 28) оставить без изменений. Применять новую стратегию хэштегов для контента после 29 октября 2025.

---

# VI. БУДУЩЕЕ И МАСШТАБИРОВАНИЕ

## 24. ПОТЕНЦИАЛЬНЫЕ УЛУЧШЕНИЯ

```yaml
future_considerations:
  potential_enhancements:
    - "Добавление английского языка"
    - "Галерея изображений прошлых туров"
    - "Отзывы участников"
    - "Календарь будущих дат"
    - "Интеграция с платежной системой"
  
  technical_debt:
    status: "Минимальный"
    reason: "Архитектура чистая и простая"
  
  scalability:
    - "Легко масштабируется на другие туры/программы"
    - "Шаблон может быть переиспользован"
    - "Единый бренд Paris Design Tours"
  
  instagram_strategy_next:
    - "Reels с личным контентом Ольги (behind the scenes)"
    - "Карусели с образовательным контентом (фигуры, концепции)"
    - "Stories с регулярностью (2-3 раза в неделю)"
    - "Публикации в пик активности (Вт-Чт, 18:00-21:00)"
```

---

# VII. МЕТА-ВОПРОСЫ ДЛЯ AI-АГЕНТА

## 25. САМОПРОВЕРКА

После каждой операции задать себе:

```yaml
meta_questions:
  q0: "ЗАБОТА О ЗРИТЕЛЕ И СОЗДАТЕЛЕ?"
  q1: "МОЖНО ЛИ БЕЗ ЭТОГО ОБОЙТИСЬ?"
  q2: "Практика = теории?"
  q3: "Сигнал/шум максимален?"
  q4: "Архитектура наивысшего качества?"
  
  action: "Если хотя бы один ответ «нет» — исправлять немедленно"
```

---

# VIII. КОММУНИКАЦИЯ AI-АГЕНТОВ

## 27. ПРОТОКОЛ СВЯЗИ GEMINI ↔ CLAUDE

**Статус**: ✅ **Успешно валидирован** (28-29 октября 2025)

**Артефакты**:
- `HANDSHAKE_V3_RESPONSE.md` (первая итерация, partial)
- `HANDSHAKE_V4_RESPONSE.md` (корректирующая итерация, full compliance)
- `GEMINI_CONFIRMATION_V4_COMPLETE.md` (финальное подтверждение Gemini)

**Протокол**:
```yaml
communication_protocol:
  initiator: Gemini
  target: Claude 4.5 Sonnet
  intermediary: User_Relay
  
  ground_truth_hierarchy:
    priority_1: "Curator Feedback (CONTEXT_DATA 2.0, скриншоты)"
    priority_2: "PROJECT_KNOWLEDGE.md (канонический контекст)"
    priority_3: "User_Relay transmission (канал, НЕ источник)"
  
  validation_cycle:
    phase_1: "V3 — Частичная имплементация (7/7 actions, 2 ошибки)"
    phase_2: "V4 — Корректирующая итерация (100% fidelity)"
    phase_3: "Confirmation — Gemini подтверждает соответствие"
  
  error_learnings:
    error_3_5:
      mistake: "Принял User_Relay statement как Ground Truth override"
      correction: "Curator Feedback = приоритет #1"
    
    error_3_7:
      mistake: "Низкий signal/noise ratio (поэтичность > специфичность)"
      correction: "Конкретные исторические якоря (Jean Désert, 1922)"
  
  channel_status: "Operational"
  next_ready: "TASK V5 (awaiting Gemini directive)"
```

**Уроки**:
1. **Ground Truth иерархия** критична: Curator Feedback > PK.md > User_Relay
2. **Специфичность > Поэтичность** в фактических описаниях (PK.md §25, q3)
3. **Критические элементы** (форма) требуют отдельной документации и процедур

**Fidelity**: 100% (V4)  
**Latency**: ~20 минут (V3 → V4 correction)  
**Robustness**: Валидирована через correction cycle

---

# IX. ИНДЕКС

```yaml
quick_reference:
  critical_rules: "§5"
  architecture: "§2"
  workflow: "§2"
  content_strategy: "§4"
  curators: "§15"
  program: "§17"
  source_materials: "§19"
  quotes: "§20"
  anti_patterns: "§7"
  operational_model: "§12"
  website_content_changes: "§18"
  instagram_campaign: "§26"
  form_procedure: "§5 (rule_009), §18 (artifact)"
  ai_communication_protocol: "§27"
```

---

**КОНЕЦ ЕДИНОГО ДОКУМЕНТА ЗНАНИЙ**

---

**Версия:** 2.2-ig-strategy  
**Дата:** 29 октября 2025  
**Обновления с v2.1:**
- §15 (Ольга Розет): Добавлен статус "Художник" + метрики профиля (955 posts, 8,419 followers, 2,006 following, ссылка parisinjanuary.ru)
- **NEW §26.6**: IG Promotion Guide Summary (резюме "Простого гида...", алгоритм 2025, форматы, Discovery)
- **NEW §26.7**: Refined IG Strategy (Gemini Vision) — двухцелевая стратегия (Удержание/Рост), форматы Reels/Stories/Карусели (40/40/20), частота/время, CTA, метрики
- **NEW §26.8**: Hashtag Analysis — анализ текущих 16 хэштегов, рекомендация 3-5 узких для будущих постов

**Обновления с v2.0:**
- §1: Добавлена каноническая связка Фигура—Концепция + ось "Человечность"
- §4: Добавлен принцип "Без избыточности" для промо-контента
- §5: Добавлено правило rule_009 (форма = постоянный приоритет)
- §12: meta_question изменен с q1 на q0 ("Забота о Зрителе и Создателе")
- §18: Детализированы 5 ключевых изменений WEBSITE_CONTENT.md (commit 2c213c9) + FORM_CHECK_PROCEDURE.md
- **§26**: INSTAGRAM КАМПАНИЯ (8 подразделов: Font Analysis, Font Decision, Stories, Post, Insights, Guide Summary, Strategy, Hashtag Analysis)
- **§27**: КОММУНИКАЦИЯ AI-АГЕНТОВ (протокол Gemini↔Claude, статус валидирован)

**Составлено**: Интеграция v2.1 + NEW_GROUND_TRUTH_DATA_V2.2 (29 Oct 2025)  
**Статус**: Canonical source of truth  
**Следующее обновление**: По мере эволюции проекта или TASK V26 от Gemini

