#!/usr/bin/env python3
"""
Тесты на краевые кейсы парсинга build.py
Priority #4 из AI_DEV_BRIEF: покрыть вариативность Markdown
"""

import sys
import tempfile
from pathlib import Path

# Import build.py functions
sys.path.insert(0, str(Path(__file__).parent))
from build import parse_content, apply_russian_typography

def test_hero_with_extra_whitespace():
    """Тест: лишние пробелы и переносы в hero секции"""
    content = """---
title: "Test"
version: "test"
---

# Индивидуальный почерк ар-деко<br><span class="hero-accent">100 лет</span>


Фактуры, материалы, атмосфера. 


15–18+ января 2026   |   до 12 человек   |  1 550 €

## Программа

Test content
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'hero' in data
    assert data['hero']['dates'] == '15–18+ января 2026'
    # Типографика применяется - ожидаем &nbsp;
    assert data['hero']['group'] == 'до&nbsp;12 человек'
    assert data['hero']['price'] == '1 550&nbsp;€'
    print("✅ Hero с extra whitespace")

def test_hero_with_multiline_subtitle():
    """Тест: многострочный subtitle"""
    content = """---
title: "Test"
version: "test"
---

# Title

Line 1
Line 2
Line 3

15–18 января 2026 | до 12 человек | 1 550 €

## Программа

Test
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'hero' in data
    assert '<br>' in data['hero']['subtitle']
    print("✅ Hero с multiline subtitle")

def test_day_without_theme():
    """Тест: день без **Тема:**"""
    content = """---
title: "Test"
version: "test"
---

# Title

Subtitle

15–18 января 2026 | до 12 человек | 1 550 €

## Программа

Intro

---

## ДЕНЬ I • 15 января
### ЗАГОЛОВОК ДНЯ

**Location Name**

Description of location

---

## Кураторы

### Name

• Bio item

---
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'days' in data
    assert len(data['days']) > 0
    assert data['days'][0]['theme'] == ''
    print("✅ День без темы")

def test_location_with_empty_lines():
    """Тест: локация с пустыми строками в описании"""
    content = """---
title: "Test"
version: "test"
---

# Title

Subtitle

15–18 января 2026 | до 12 человек | 1 550 €

## Программа

Intro

---

## ДЕНЬ I • 15 января
### DAY TITLE

**Location**

First paragraph.

Second paragraph after empty line.

Third paragraph.

---

## Кураторы

### Name

• Bio

---
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'days' in data
    assert len(data['days']) > 0
    assert len(data['days'][0]['locations']) > 0
    # Парсер должен сохранить структуру с пустыми строками
    assert '\n' in data['days'][0]['locations'][0]['description']
    print("✅ Локация с пустыми строками")

def test_curator_without_role():
    """Тест: куратор без **Роль:**"""
    content = """---
title: "Test"
version: "test"
---

# Title

Subtitle

15–18 января 2026 | до 12 человек | 1 550 €

## Программа

Intro

---

## ДЕНЬ I • 15 января
### DAY TITLE

**Location**
Description

---

## Кураторы

### Curator Name

• Bio item 1
• Bio item 2

**В программе:**
Program description

---
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'curators' in data
    assert len(data['curators']) > 0
    assert data['curators'][0]['role'] == ''
    assert data['curators'][0]['name'] == 'Curator Name'
    print("✅ Куратор без роли")

def test_typography_with_html_tags():
    """Тест: типографика не ломает HTML теги"""
    text = '<span class="emphasis">Test "quotes" and — dashes</span>'
    result = apply_russian_typography(text)
    
    # HTML теги должны остаться нетронутыми
    assert '<span class="emphasis">' in result
    assert '</span>' in result
    # Кавычки внутри должны быть заменены
    assert '«' in result or '»' in result
    print("✅ Типографика с HTML тегами")

def test_typography_nbsp_after_prepositions():
    """Тест: неразрывные пробелы после предлогов"""
    text = "Это и то в доме на столе"
    result = apply_russian_typography(text)
    
    # После предлогов должен быть &nbsp;
    assert 'и&nbsp;' in result
    assert 'в&nbsp;' in result
    assert 'на&nbsp;' in result
    print("✅ Неразрывные пробелы после предлогов")

def test_program_intro_with_blockquotes():
    """Тест: intro с > blockquotes"""
    content = """---
title: "Test"
version: "test"
---

# Title

Subtitle

15–18 января 2026 | до 12 человек | 1 550 €

## Программа

Normal paragraph.

> **Highlighted quote**

Another paragraph.

---

## ДЕНЬ I • 15 января
### DAY

**Loc**
Desc

---

## Кураторы

### Name
• Bio

---
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    assert 'program' in data
    assert 'intro' in data['program']
    
    # Должен быть highlight item
    highlights = [item for item in data['program']['intro'] if isinstance(item, dict) and item.get('type') == 'highlight']
    assert len(highlights) > 0
    print("✅ Program intro с blockquotes")

def test_missing_sections():
    """Тест: отсутствующие опциональные секции"""
    content = """---
title: "Test"
version: "test"
---

# Title

Subtitle

15–18 января 2026 | до 12 человек | 1 550 €
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        data = parse_content(f.name)
        Path(f.name).unlink()
    
    # Парсер должен создать пустые структуры для отсутствующих секций
    assert 'hero' in data
    assert 'meta' in data
    assert 'program' in data
    assert 'days' in data
    assert 'curators' in data
    print("✅ Отсутствующие опциональные секции")

def test_alternative_date_formats():
    """Тест: альтернативные форматы дат с учетом типографики"""
    dates_variants = [
        ("15-18 января 2026", "15−18 января 2026"),  # обычный дефис → минус
        ("15 – 18 января 2026", "15 – 18 января 2026"),  # длинное тире уже есть, не меняется
        ("15–18+ января 2026", "15–18+ января 2026"),  # с плюсом
        ("15–18 янв 2026", "15–18 янв 2026"),  # сокращение
    ]
    
    for input_date, expected_date in dates_variants:
        content = f"""---
title: "Test"
version: "test"
---

# Title

Subtitle

{input_date} | до 12 человек | 1 550 €

## Программа
Test
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(content)
            f.flush()
            data = parse_content(f.name)
            Path(f.name).unlink()
        
        assert 'hero' in data
        # Типографика применяется: дефис → минус, пробелы вокруг тире
        assert data['hero']['dates'] == expected_date, f"Expected '{expected_date}', got '{data['hero']['dates']}'"
    
    print("✅ Альтернативные форматы дат")

if __name__ == '__main__':
    print("🧪 ТЕСТИРОВАНИЕ КРАЕВЫХ КЕЙСОВ build.py\n")
    
    tests = [
        test_hero_with_extra_whitespace,
        test_hero_with_multiline_subtitle,
        test_day_without_theme,
        test_location_with_empty_lines,
        test_curator_without_role,
        test_typography_with_html_tags,
        test_typography_nbsp_after_prepositions,
        test_program_intro_with_blockquotes,
        test_missing_sections,
        test_alternative_date_formats,
    ]
    
    failed = []
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"❌ {test.__name__}: {e}")
            failed.append(test.__name__)
        except Exception as e:
            print(f"💥 {test.__name__}: {e}")
            failed.append(test.__name__)
    
    print("\n" + "="*60)
    if failed:
        print(f"❌ ПРОВАЛЕНО: {len(failed)}/{len(tests)}")
        for name in failed:
            print(f"   - {name}")
        sys.exit(1)
    else:
        print(f"✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ ({len(tests)}/{len(tests)})")
        sys.exit(0)

