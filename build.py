#!/usr/bin/env python3
"""
Генератор всех страниц parisinjanuary.ru из единого content.md
Генерирует: index.html, support/index.html, support/hotels/index.html
"""

import re
import markdown
from pathlib import Path

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

<script>
// Автоматическое версионирование для обхода кеша
(function() {{
  const url = new URL(window.location.href);
  const hasVersion = url.searchParams.has('v');
  if (!hasVersion) {{
    url.searchParams.set('v', Date.now());
    window.history.replaceState({{}}, '', url);
  }}
}})();
</script>

</body>
</html>'''

# Сохраняем index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('✅ index.html сгенерирован')

# === ГЕНЕРАЦИЯ SUPPORT/INDEX.HTML ===

support_sections = re.split(r'^### ', support_content, flags=re.MULTILINE)
support_sections = [s.strip() for s in support_sections if s.strip()]

support_nav = '<ul>\n'
for section in support_sections:
    if section.startswith('Отели'):
        support_nav += '  <li><a href="./hotels/">Отели</a></li>\n'
    elif section.startswith('Транспорт'):
        support_nav += '  <li><a href="./transport/">Транспорт</a> <em>(скоро)</em></li>\n'
    elif section.startswith('Практическая информация'):
        support_nav += '  <li><a href="./info/">Практическая информация</a> <em>(скоро)</em></li>\n'
support_nav += '</ul>'

support_index_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Поддержка участников — Paris January 2026</title>
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

a {{
  color: #2c5aa0;
  text-decoration: none;
  border-bottom: 1px solid #2c5aa0;
}}

a:hover {{
  border-bottom-color: var(--accent-red);
}}

ul {{
  list-style: none;
  padding: 0;
}}

li {{
  padding: 0.75rem 0;
  border-bottom: 1px solid #f0f0f0;
}}

li:last-child {{
  border-bottom: none;
}}

em {{
  color: var(--text-muted);
  font-style: normal;
  font-size: 0.9rem;
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

  <nav>
    <h2>Разделы</h2>
    {support_nav}
  </nav>

  <div class="contact">
    <h2>Остались вопросы?</h2>
    <p>Ольга всегда готова помочь</p>
    <p><a href="https://t.me/olga_rozet">Написать в Telegram →</a></p>
  </div>
</div>

<script>
// Автоматическое версионирование для обхода кеша
(function() {{
  const url = new URL(window.location.href);
  const hasVersion = url.searchParams.has('v');
  if (!hasVersion) {{
    url.searchParams.set('v', Date.now());
    window.history.replaceState({{}}, '', url);
  }}
}})();
</script>

</body>
</html>'''

Path('support').mkdir(exist_ok=True)
with open('support/index.html', 'w', encoding='utf-8') as f:
    f.write(support_index_html)

print('✅ support/index.html сгенерирован')

# === ГЕНЕРАЦИЯ SUPPORT/HOTELS/INDEX.HTML ===

# Находим секцию Отели
hotels_content = ''
for section in support_sections:
    if section.startswith('Отели'):
        hotels_content = section
        break

# Парсим содержимое отелей
hotels_parts = re.split(r'^#### ', hotels_content, flags=re.MULTILINE)
hotels_parts = [p.strip() for p in hotels_parts if p.strip()]

hotels_html_parts = {}

for part in hotels_parts:
    if part.startswith('17 проверенных отелей'):
        hotels_html_parts['intro'] = part
    elif part.startswith('Совет'):
        hotels_html_parts['tip'] = part.replace('Совет\\n\\n', '')
    elif part.startswith('Почему именно эти районы'):
        hotels_html_parts['why'] = part
    elif part.startswith('Как выбрать свой отель'):
        hotels_html_parts['how'] = part
    elif part.startswith('Нужна помощь с выбором?'):
        hotels_html_parts['help'] = part

hotels_page_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Отели Парижа — Поддержка участников | Paris January 2026</title>
<meta name="description" content="Проверенные отели для участников дизайн-путешествия в Париж, январь 2026">
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

h2 {{
  font-family: var(--font-display);
  font-size: 1.8rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem;
}}

.subtitle {{
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 3rem;
}}

.tip {{
  background: #fafafa;
  border-left: 3px solid var(--accent-red);
  padding: 1.5rem 1.8rem;
  margin: 2.5rem 0;
  line-height: 1.7;
}}

.tip strong {{
  font-weight: 600;
  color: var(--midnight-blue);
}}

.note {{
  color: var(--text-muted);
  font-size: 0.95rem;
  margin: 1rem 0;
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
</style>
</head>
<body>

<div class="container">
  <h1>Отели Парижа</h1>
  <p class="subtitle">Поддержка участников</p>

  <div class="tip">
    <strong>Совет:</strong> {hotels_html_parts.get('tip', '')}
  </div>

  <h2>17 проверенных отелей</h2>
  {markdown.markdown(hotels_html_parts.get('intro', ''))}

  <h2>Почему именно эти районы</h2>
  {markdown.markdown(hotels_html_parts.get('why', ''))}

  <h2>Как выбрать свой отель</h2>
  {markdown.markdown(hotels_html_parts.get('how', ''))}

  <h2>Нужна помощь с выбором?</h2>
  {markdown.markdown(hotels_html_parts.get('help', ''))}

</div>

<script>
// Автоматическое версионирование для обхода кеша
(function() {{
  const url = new URL(window.location.href);
  const hasVersion = url.searchParams.has('v');
  if (!hasVersion) {{
    url.searchParams.set('v', Date.now());
    window.history.replaceState({{}}, '', url);
  }}
}})();
</script>

</body>
</html>'''

Path('support/hotels').mkdir(parents=True, exist_ok=True)
with open('support/hotels/index.html', 'w', encoding='utf-8') as f:
    f.write(hotels_page_html)

print('✅ support/hotels/index.html сгенерирован')
print(f'\n�� Все страницы сгенерированы из content.md (версия {version})')
