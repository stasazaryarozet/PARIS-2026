#!/usr/bin/env python3
"""
Instagram Stories Generator
Генерирует триптих из 3 сториз для Paris January 2026
Минимальные зависимости: только Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
from pathlib import Path

# Константы
STORY_SIZE = (1080, 1920)
OUTPUT_DIR = Path(__file__).parent.parent / "instagram_stories"

# Цветовая палитра проекта
COLORS = {
    "midnight_blue": "#0A2342",
    "warm_white": "#F8F6F3",
    "accent_red": "#E31B1B",
    "charcoal": "#2C2C2C",
}

def hex_to_rgb(hex_color):
    """Конвертирует HEX в RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def draw_text_centered(draw, text, y_position, font, fill, image_width):
    """Рисует текст по центру"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (image_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=fill)

def draw_text_multiline(draw, text, y_position, font, fill, image_width, max_width):
    """Рисует многострочный текст с переносами"""
    lines = textwrap.wrap(text, width=max_width)
    current_y = y_position
    
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (image_width - text_width) // 2
        draw.text((x, current_y), line, font=font, fill=fill)
        current_y += text_height + 20
    
    return current_y

def get_font(size, bold=False):
    """Получает шрифт (системный fallback)"""
    try:
        # Попытка использовать системные шрифты
        if bold:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        # Fallback на дефолтный
        return ImageFont.load_default()

def generate_story_1():
    """Story 1: Захват (Hook) - Философский вопрос"""
    img = Image.new('RGB', STORY_SIZE, hex_to_rgb(COLORS["midnight_blue"]))
    draw = ImageDraw.Draw(img)
    
    # Шрифты
    font_large = get_font(140, bold=True)
    font_medium = get_font(96)
    font_small = get_font(48)
    
    # Текст
    draw_text_centered(draw, "Необходим ли", 600, font_medium, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    draw_text_centered(draw, "КОНТАКТ", 780, font_large, 
                      hex_to_rgb(COLORS["accent_red"]), STORY_SIZE[0])
    
    draw_text_centered(draw, "С РЕАЛЬНОСТЬЮ", 940, font_large, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    draw_text_centered(draw, "?", 1100, font_large, 
                      hex_to_rgb(COLORS["accent_red"]), STORY_SIZE[0])
    
    # Подпись снизу
    draw_text_centered(draw, "Можно ли ощутить словами?", 1700, font_small, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    return img

def generate_story_2():
    """Story 2: Ценность (Value) - Цитата куратора"""
    img = Image.new('RGB', STORY_SIZE, hex_to_rgb(COLORS["warm_white"]))
    draw = ImageDraw.Draw(img)
    
    # Шрифты
    font_quote = get_font(64)
    font_author = get_font(56)
    font_details = get_font(48)
    
    # Цитата (многострочная)
    quote = '"Мы будем в интерьерах смотреть секреты мастеров. Соотношения фактуры текстур, тонкости цвета — то, что не видно ни в одной публикации"'
    
    # Разбиваем цитату вручную для лучшего контроля
    y = 400
    lines = [
        '"Мы будем в интерьерах',
        'смотреть секреты мастеров.',
        '',
        'Соотношения фактуры текстур,',
        'тонкости цвета —',
        '',
        'то, что не видно',
        'ни в одной публикации"'
    ]
    
    for line in lines:
        if line:  # Пропускаем пустые строки для отступа
            draw_text_centered(draw, line, y, font_quote, 
                             hex_to_rgb(COLORS["charcoal"]), STORY_SIZE[0])
        y += 85
    
    # Автор
    draw_text_centered(draw, "— Ольга Розет", y + 60, font_author, 
                      hex_to_rgb(COLORS["accent_red"]), STORY_SIZE[0])
    
    # Детали снизу
    draw_text_centered(draw, "Париж • 15–18 января 2026", 1700, font_details, 
                      hex_to_rgb(COLORS["charcoal"]), STORY_SIZE[0])
    
    return img

def generate_story_3():
    """Story 3: Действие (CTA) - Призыв к действию"""
    img = Image.new('RGB', STORY_SIZE, hex_to_rgb(COLORS["accent_red"]))
    draw = ImageDraw.Draw(img)
    
    # Шрифты
    font_title = get_font(90)
    font_large = get_font(120, bold=True)
    font_medium = get_font(70)
    font_small = get_font(56)
    font_url = get_font(60, bold=True)
    
    # Заголовок
    y = 400
    draw_text_centered(draw, "Индивидуальный почерк", y, font_title, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    y += 100
    draw_text_centered(draw, "ар-деко", y, font_title, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    # 100 лет (главный акцент)
    y += 150
    draw_text_centered(draw, "100 ЛЕТ", y, font_large, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    # Детали
    y += 180
    draw_text_centered(draw, "4 дня с Ольгой Розет", y, font_medium, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    y += 90
    draw_text_centered(draw, "и Натальей Логиновой", y, font_medium, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    # Условия
    y += 140
    draw_text_centered(draw, "До 12 человек", y, font_small, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    y += 80
    draw_text_centered(draw, "1 550 €", y, font_small, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    # CTA
    y += 140
    draw_text_centered(draw, "↑ Свайп вверх", y, font_medium, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    y += 90
    draw_text_centered(draw, "parisinjanuary.ru", y, font_url, 
                      hex_to_rgb(COLORS["warm_white"]), STORY_SIZE[0])
    
    return img

def main():
    """Генерирует все 3 сториз"""
    # Создаём директорию
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("Генерация Instagram Stories...")
    print(f"Размер: {STORY_SIZE[0]}x{STORY_SIZE[1]}px")
    print(f"Выходная директория: {OUTPUT_DIR}")
    print()
    
    # Story 1
    print("→ Story 1: Hook (Философский вопрос)...")
    story1 = generate_story_1()
    story1_path = OUTPUT_DIR / "story_1_hook.png"
    story1.save(story1_path, "PNG", quality=95)
    print(f"  Сохранено: {story1_path}")
    
    # Story 2
    print("→ Story 2: Value (Цитата куратора)...")
    story2 = generate_story_2()
    story2_path = OUTPUT_DIR / "story_2_value.png"
    story2.save(story2_path, "PNG", quality=95)
    print(f"  Сохранено: {story2_path}")
    
    # Story 3
    print("→ Story 3: CTA (Призыв к действию)...")
    story3 = generate_story_3()
    story3_path = OUTPUT_DIR / "story_3_cta.png"
    story3.save(story3_path, "PNG", quality=95)
    print(f"  Сохранено: {story3_path}")
    
    print()
    print("✓ Готово! 3 сториз сгенерированы.")
    print()
    print("Следующий шаг:")
    print("1. Загрузить в Instagram как Stories")
    print("2. На Story 3 добавить Link Sticker с URL: https://parisinjanuary.ru")
    print("3. Опубликовать последовательно (1→2→3)")

if __name__ == "__main__":
    main()

