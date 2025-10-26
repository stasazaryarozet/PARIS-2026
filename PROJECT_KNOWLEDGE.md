---
meta:
  project: paris-2026
  version: 2.0-unified
  created: 2025-10-26
  format: Markdown + YAML
  purpose: Единый источник знаний о проекте для AI-агентов и людей
  encoding: UTF-8
---

# PROJECT KNOWLEDGE — Единый источник правды

**Версия:** 2.0 (объединённая)  
**Дата:** 26 октября 2025  
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
      - v178-headers-larger
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
  
  current_version: v179-hide-badge
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
    PROJECT_KNOWLEDGE.md: "Этот файл - единый источник знаний"
    AI_COMMUNICATION_LOG.md: "История взаимодействий и решений"
    TO_GEMINI.md: "Инструкции для AI-ассистентов"
  
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
    pattern: "Frontend form → Formspree API → Email notification"
    validation: "Двойная валидация (клиент + сервер)"
    ux: "Модальное окно с состояниями"
```

---

## 12. ОПЕРАЦИОННАЯ МОДЕЛЬ AI-АГЕНТА

### Основополагающий принцип

**Решение минимальными средствами или их отсутствием.**

```yaml
core_principle:
  philosophy: "Обходимся без всего, без чего можно обойтись"
  
  ideals:
    - "Идеальный компонент — отсутствующий"
    - "Идеальная строка кода — ненаписанная"
    - "Идеальная зависимость — отсутствующая"
    - "Идеальная сложность — отсутствие сложности"
  
  meta_question: "МОЖНО ЛИ БЕЗ ЭТОГО ОБОЙТИСЬ?"
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
    loop: "Вернуться к Шагу 1"
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
    
    - name: "Eileen Gray"
      style: "Модернизм через эргономику"
      signature: "Наблюдение за поведением человека"
    
    - name: "Alvar Aalto"
      style: "Органический модернизм"
      signature: "Эргономика как забота"
  
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
    - "Работала в Музее декоративно-прикладного искусства"
  
  current_status:
    location: "Иммигрировала в Париж"
    reason: "Любовь к городу"
    activity: "Авторские туры по дизайну и архитектуре"
  
  expertise:
    - "Секретные крыши Парижа"
    - "Витражи"
    - "Детали архитектуры"
    - "Неочевидные места"
  
  role_in_program:
    - "Локальная навигация (резидент Парижа)"
    - "Выбор музея для Дня I"
    - "Связь с владелицей Galerie Vallois"
    - "Маршрут выставки 1937"
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

---

### ДЕНЬ II • 16 января — Левый берег

**Saint-Germain-des-Prés**
- Rue de Seine — квартал антикваров с 1970-х
- Лак, хром, фанеровка

**Galerie Vallois (41 rue de Seine)**
- Робер Валлуа (открыта 1971)
- Эйлин Грей: столик E-1027, кресло Transat, ширма Briques
- Рульманн, Дюнан, Пьер Шаро

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
- Разговор

---

## 18. КОНТЕНТ САЙТА (WEBSITE_CONTENT.md)

```yaml
website_content:
  version: 66
  url: https://parisinjanuary.ru
  
  meta:
    title: "Индивидуальный почерк ар-деко. 100 лет — 4 дня в Париже (январь 2026)"
    description: "4 дня в Париже. Фактуры, материалы, атмосфера. Ольга Розет и Наталья Логинова."
    og_image: "https://parisinjanuary.ru/og-image.jpg"
```

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

# V. БУДУЩЕЕ И МАСШТАБИРОВАНИЕ

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
```

---

# VI. МЕТА-ВОПРОСЫ ДЛЯ AI-АГЕНТА

## 25. САМОПРОВЕРКА

После каждой операции задать себе:

```yaml
meta_questions:
  q1: "МОЖНО ЛИ БЕЗ ЭТОГО ОБОЙТИСЬ?"
  q2: "Практика = теории?"
  q3: "Сигнал/шум максимален?"
  q4: "Архитектура наивысшего качества?"
  
  action: "Если хотя бы один ответ «нет» — исправлять немедленно"
```

---

# VII. ИНДЕКС

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
```

---

**КОНЕЦ ЕДИНОГО ДОКУМЕНТА ЗНАНИЙ**

---

**Версия:** 2.0-unified  
**Дата:** 26 октября 2025  
**Составлено:** Объединение PROJECT_KNOWLEDGE_GRAPH.json + PROJECT_KNOWLEDGE_BASE.md  
**Статус:** Canonical source of truth  
**Следующее обновление:** По мере эволюции проекта
