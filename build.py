#!/usr/bin/env python3
"""
Генератор всех страниц parisinjanuary.ru из единого content.md
Генерирует: index.html, support/index.html (плоская страница)
"""

import re
import markdown
from pathlib import Path
import shutil

# Скрипт для обхода кеша (единый для всех страниц)
CACHE_BUST_SCRIPT = """<script>
// Обход кеша через случайный параметр при fetch, чистый URL в адресной строке
(function() {
  const url = new URL(window.location.href);
  
  // Если есть параметр кеш-бастинга, убираем его из адресной строки
  if (url.searchParams.has('_') || url.searchParams.has('v') || url.searchParams.has('_t')) {
    url.searchParams.delete('_');
    url.searchParams.delete('v');
    url.searchParams.delete('_t');
    window.history.replaceState({}, '', url.pathname);
  }
})();
</script>"""

# Читаем content.md
content_path = Path(__file__).parent / 'content.md'
with open(content_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Парсим frontmatter
frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
if frontmatter_match:
    frontmatter = frontmatter_match.group(1)
    version_match = re.search(r'version:\s*(.+)', frontmatter)
    version = version_match.group(1).strip() if version_match else '1.0'
    content_body = content[frontmatter_match.end():]
else:
    version = '1.0'
    content_body = content

# Разделяем на секции
sections = re.split(r'^# ', content_body, flags=re.MULTILINE)
sections = [s.strip() for s in sections if s.strip()]

# Находим секции
landing_content = ''
support_content = ''

for section in sections:
    if section.startswith('Париж в Январе 2026'):
        landing_content = section
    elif section.startswith('Support'):
        support_content = section

# === ГЕНЕРАЦИЯ INDEX.HTML (посадочная) ===

# Парсим landing_content
landing_parts = re.split(r'^## ', landing_content, flags=re.MULTILINE)
landing_parts = [p.strip() for p in landing_parts if p.strip()]

# Извлекаем данные
program_html = ''
details_html = ''
consultation_html = ''

for part in landing_parts:
    if part.startswith('Программа'):
        # Парсим программу
        program_items = re.findall(r'^### (.+?)\n(.+?)(?=\n###|\n##|$)', part, re.MULTILINE | re.DOTALL)
        program_html = '<div class="program">\n'
        for title, desc in program_items:
            program_html += f'  <div class="program-item">\n'
            program_html += f'    <h3>{title.strip()}</h3>\n'
            program_html += f'    <p>{desc.strip()}</p>\n'
            program_html += f'  </div>\n'
        program_html += '</div>'
    
    elif part.startswith('Детали'):
        details_html = markdown.markdown(part)
    
    elif part.startswith('Консультация'):
        consultation_html = markdown.markdown(part)

# Генерируем index.html
index_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Париж в Январе 2026 — Дизайн-путешествие с Ольгой Розет</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
  <h1>Париж в Январе 2026</h1>
  <p class="subtitle">Дизайн-путешествие</p>
  <p>Неделя в Париже: музеи, галереи, мастерские дизайнеров.</p>
  <p><strong>Даты:</strong> 13–19 января 2026<br>
  <strong>Ведущая:</strong> Ольга Розет — художник, искусствовед</p>
</header>

<main>
  <section id="program">
    <h2>Программа</h2>
    {program_html}
  </section>

  <section id="details">
    <h2>Детали</h2>
    {details_html}
  </section>

  <section id="consultation">
    {consultation_html}
  </section>

  <section id="support">
    <h2>Поддержка участников</h2>
    <p><a href="/support/">Отели, транспорт, практическая информация →</a></p>
  </section>
</main>

<footer>
  <p>v{version}</p>
</footer>

{CACHE_BUST_SCRIPT}

</body>
</html>'''

# Сохраняем index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('✅ index.html сгенерирован')

# === ГЕНЕРАЦИЯ SUPPORT/INDEX.HTML (плоская страница) ===

support_sections = re.split(r'^### ', support_content, flags=re.MULTILINE)
support_sections = [s.strip() for s in support_sections if s.strip()]

# Собираем все секции в один HTML
support_body_html = ''

for section in support_sections:
    # Пропускаем заголовок "Поддержка участников"
    if section.startswith('Поддержка участников'):
        continue
    
    # Проверяем, есть ли контент в секции (кроме заголовка)
    lines = section.split('\n', 1)
    section_title = lines[0].strip()
    section_body = lines[1].strip() if len(lines) > 1 else ''
    
    # Пропускаем пустые секции
    if not section_body:
        continue
    
    # Добавляем секцию
    support_body_html += f'<section class="support-section">\n'
    support_body_html += f'  <h2>{section_title}</h2>\n'
    
    # Парсим подсекции (#### заголовки)
    subsections = re.split(r'^#### ', section_body, flags=re.MULTILINE)
    subsections = [s.strip() for s in subsections if s.strip()]
    
    if subsections:
        for subsection in subsections:
            sub_lines = subsection.split('\n', 1)
            sub_title = sub_lines[0].strip()
            sub_body = sub_lines[1].strip() if len(sub_lines) > 1 else ''
            
            if not sub_body:
                continue
            
            # Специальная обработка для "Совет" (tip box)
            if sub_title == 'Совет':
                support_body_html += f'  <div class="tip">\n'
                support_body_html += f'    {markdown.markdown(sub_body)}\n'
                support_body_html += f'  </div>\n'
            else:
                support_body_html += f'  <h3>{sub_title}</h3>\n'
                support_body_html += f'  {markdown.markdown(sub_body)}\n'
    else:
        # Секция без подсекций
        support_body_html += f'  {markdown.markdown(section_body)}\n'
    
    support_body_html += '</section>\n\n'

support_index_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Поддержка участников — Paris January 2026</title>
<meta name="description" content="Практическая информация для участников дизайн-путешествия в Париж, январь 2026">
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=Forum&display=swap" rel="stylesheet">
<style>
:root {{
  --accent-red: #E31B1B;
  --midnight-blue: #0A2342;
  --text-primary: #000000;
  --text-muted: #666666;
  --bg-primary: #ffffff;
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

html {{
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}

body {{
  color: var(--text-primary);
  background: var(--bg-primary);
}}

.container {{
  max-width: 800px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}}

h1 {{
  font-family: var(--font-display);
  font-size: 3rem;
  font-weight: 400;
  line-height: 1.2;
  margin-bottom: 0.5rem;
}}

.subtitle {{
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 3rem;
}}

h2 {{
  font-family: var(--font-display);
  font-size: 1.8rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem;
}}

h3 {{
  font-family: var(--font-display);
  font-size: 1.3rem;
  font-weight: 600;
  margin: 2rem 0 1rem;
}}

.support-section {{
  margin-bottom: 3rem;
}}

.tip {{
  background: #fafafa;
  border-left: 3px solid var(--accent-red);
  padding: 1.5rem 1.8rem;
  margin: 2.5rem 0;
  line-height: 1.7;
  color: var(--text-primary);
}}

a {{
  color: #2c5aa0;
  text-decoration: none;
  border-bottom: 1px solid #2c5aa0;
}}

a:hover {{
  border-bottom-color: var(--accent-red);
}}

p {{
  margin: 1rem 0;
}}

strong {{
  font-weight: 600;
}}

em {{
  color: var(--text-muted);
  font-style: italic;
}}

hr {{
  border: none;
  border-top: 1px solid #e5e5e5;
  margin: 3rem 0;
}}

.contact {{
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid #e5e5e5;
}}
</style>
</head>
<body>

<div class="container">
  <h1>Поддержка участников</h1>
  <p class="subtitle">Париж в Январе 2026</p>

  {support_body_html}

  <div class="contact">
    <h2>Остались вопросы?</h2>
    <p>Ольга всегда готова помочь</p>
    <p><a href="https://t.me/olga_rozet">Написать в Telegram →</a></p>
  </div>
</div>

{CACHE_BUST_SCRIPT}

</body>
</html>'''

Path('support').mkdir(exist_ok=True)
with open('support/index.html', 'w', encoding='utf-8') as f:
    f.write(support_index_html)

print('✅ support/index.html сгенерирован (плоская страница)')

# Удаляем старую структуру support/hotels/ если существует
hotels_dir = Path('support/hotels')
if hotels_dir.exists():
    shutil.rmtree(hotels_dir)
    print('🗑️  support/hotels/ удалена (больше не нужна)')

print(f'\n🎉 Все страницы сгенерированы из content.md (версия {version})')
