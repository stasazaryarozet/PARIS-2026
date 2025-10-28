#!/usr/bin/env python3
"""
Instagram Stories Generator v2 — Geniusversion
Генерирует триптих с правильной типографикой, геометрией ар-деко и atmosphere
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import urllib.request
import os

# Константы
STORY_SIZE = (1080, 1920)
OUTPUT_DIR = Path(__file__).parent.parent / "instagram_stories"
FONTS_DIR = OUTPUT_DIR / ".fonts"

# Цветовая палитра
COLORS = {
    "midnight_blue": (10, 35, 66),
    "warm_white": (248, 246, 243),
    "accent_red": (227, 27, 27),
    "charcoal": (44, 44, 44),
    "soft_beige": (232, 228, 221),
}

# Google Fonts URLs
FONTS = {
    "cormorant_regular": "https://github.com/google/fonts/raw/main/ofl/cormorantgaramond/CormorantGaramond-Regular.ttf",
    "cormorant_bold": "https://github.com/google/fonts/raw/main/ofl/cormorantgaramond/CormorantGaramond-Bold.ttf",
    "cormorant_light": "https://github.com/google/fonts/raw/main/ofl/cormorantgaramond/CormorantGaramond-Light.ttf",
    "inter_regular": "https://github.com/google/fonts/raw/main/ofl/inter/Inter-Regular.ttf",
    "inter_medium": "https://github.com/google/fonts/raw/main/ofl/inter/Inter-Medium.ttf",
    "inter_semibold": "https://github.com/google/fonts/raw/main/ofl/inter/Inter-SemiBold.ttf",
}

def download_fonts():
    """Скачивает шрифты если их нет"""
    FONTS_DIR.mkdir(parents=True, exist_ok=True)
    
    for name, url in FONTS.items():
        font_path = FONTS_DIR / f"{name}.ttf"
        if not font_path.exists():
            print(f"  Скачиваю {name}...")
            try:
                urllib.request.urlretrieve(url, font_path)
            except Exception as e:
                print(f"  ⚠️  Ошибка загрузки {name}: {e}")

def get_font(name, size):
    """Получает шрифт с полной поддержкой кириллицы"""
    # Маппинг на шрифты с гарантированной кириллицей
    system_fonts = {
        # Serif (для заголовков) - Georgia поддерживает кириллицу
        "cormorant_regular": "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "cormorant_bold": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "cormorant_light": "/System/Library/Fonts/Supplemental/Georgia.ttf",
        # Sans (для деталей) - Helvetica Neue с полной кириллицей
        "inter_regular": "/System/Library/Fonts/Helvetica.ttc",
        "inter_medium": "/System/Library/Fonts/Helvetica.ttc",
        "inter_semibold": "/System/Library/Fonts/Helvetica.ttc",
    }
    
    # Сначала проверяем загруженные
    font_path = FONTS_DIR / f"{name}.ttf"
    if font_path.exists():
        return ImageFont.truetype(str(font_path), size)
    
    # Используем системные
    if name in system_fonts:
        try:
            return ImageFont.truetype(system_fonts[name], size)
        except:
            # Fallback на Helvetica (всегда работает с кириллицей)
            try:
                return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
            except:
                pass
    
    return ImageFont.load_default()

def draw_art_deco_lines(draw, color, style="story1"):
    """Рисует геометрические элементы ар-деко"""
    if style == "story1":
        # Тонкие линии сверху и снизу (с safe zones)
        draw.line([(120, 450), (960, 450)], fill=color, width=2)
        draw.line([(120, 1500), (960, 1500)], fill=color, width=2)
        
        # Угловые акценты
        draw.line([(120, 450), (120, 500)], fill=color, width=2)
        draw.line([(960, 450), (960, 500)], fill=color, width=2)
        draw.line([(120, 1500), (120, 1450)], fill=color, width=2)
        draw.line([(960, 1500), (960, 1450)], fill=color, width=2)
    
    elif style == "story2":
        # Вертикальная линия слева (с safe zone)
        draw.rectangle([(100, 400), (110, 1200)], fill=color)
    
    elif style == "story3":
        # Рамка (с safe zones)
        margin = 100
        draw.line([(margin, margin), (1080-margin, margin)], fill=COLORS["warm_white"], width=3)
        draw.line([(margin, margin), (margin, 1920-margin)], fill=COLORS["warm_white"], width=3)
        draw.line([(1080-margin, margin), (1080-margin, 1920-margin)], fill=COLORS["warm_white"], width=3)
        draw.line([(margin, 1920-margin), (1080-margin, 1920-margin)], fill=COLORS["warm_white"], width=3)

def draw_centered_text(draw, text, y, font, color, image_width, letter_spacing=0):
    """Рисует текст по центру с tracking"""
    if letter_spacing == 0:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (image_width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
    else:
        # С letter spacing
        total_width = sum(draw.textbbox((0, 0), char, font=font)[2] - 
                         draw.textbbox((0, 0), char, font=font)[0] + letter_spacing 
                         for char in text) - letter_spacing
        x = (image_width - total_width) // 2
        for char in text:
            draw.text((x, y), char, font=font, fill=color)
            char_width = draw.textbbox((0, 0), char, font=font)[2] - draw.textbbox((0, 0), char, font=font)[0]
            x += char_width + letter_spacing

def generate_story_1_genius():
    """Story 1: Философский вопрос с геометрией ар-деко"""
    img = Image.new('RGB', STORY_SIZE, COLORS["midnight_blue"])
    draw = ImageDraw.Draw(img)
    
    # Геометрические элементы
    draw_art_deco_lines(draw, COLORS["warm_white"], "story1")
    
    # Шрифты
    font_small = get_font("inter_regular", 50)
    font_large = get_font("cormorant_bold", 150)
    font_question = get_font("cormorant_light", 190)
    font_subtitle = get_font("inter_light", 42) if (FONTS_DIR / "inter_light.ttf").exists() else get_font("inter_regular", 42)
    
    # Композиция (с safe zones)
    y = 580
    
    # "Необходим ли" — тонко, сверху
    draw_centered_text(draw, "Необходим ли", y, font_small, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=8)
    
    y += 140
    # "КОНТАКТ" — красный акцент
    draw_centered_text(draw, "КОНТАКТ", y, font_large, COLORS["accent_red"], STORY_SIZE[0], letter_spacing=20)
    
    y += 180
    # "С РЕАЛЬНОСТЬЮ" — белый
    draw_centered_text(draw, "С РЕАЛЬНОСТЬЮ", y, font_large, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=12)
    
    y += 220
    # "?" — огромный, тонкий
    draw_centered_text(draw, "?", y, font_question, COLORS["accent_red"], STORY_SIZE[0])
    
    # Подпись снизу (с safe zone)
    draw_centered_text(draw, "Можно ли ощутить словами?", 1420, font_subtitle, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=4)
    
    return img

def generate_story_2_genius():
    """Story 2: Цитата с editorial layout"""
    img = Image.new('RGB', STORY_SIZE, COLORS["warm_white"])
    draw = ImageDraw.Draw(img)
    
    # Геометрический элемент
    draw_art_deco_lines(draw, COLORS["accent_red"], "story2")
    
    # Шрифты
    font_quote = get_font("cormorant_light", 68)
    font_author = get_font("inter_semibold", 52)
    font_details = get_font("inter_regular", 42)
    
    # Цитата с правильным line-height и safe zones
    y = 450
    padding_left = 160
    padding_right = 100
    line_height = 92
    
    lines = [
        '"Мы будем в интерьерах',
        'смотреть секреты мастеров.',
        '',
        'Соотношения фактуры',
        'текстур, тонкости цвета —',
        '',
        'то, что не видно',
        'ни в одной публикации"'
    ]
    
    for line in lines:
        if line:
            draw.text((padding_left, y), line, font=font_quote, fill=COLORS["charcoal"])
        y += line_height
    
    # Автор
    y += 80
    draw.text((padding_left, y), "— Ольга Розет", font=font_author, fill=COLORS["accent_red"])
    
    # Детали снизу (с safe zone)
    draw_centered_text(draw, "Париж • 15–18 января 2026", 1700, font_details, COLORS["charcoal"], STORY_SIZE[0], letter_spacing=3)
    
    return img

def generate_story_3_genius():
    """Story 3: CTA с sophisticated layout"""
    img = Image.new('RGB', STORY_SIZE, COLORS["accent_red"])
    draw = ImageDraw.Draw(img)
    
    # Геометрическая рамка
    draw_art_deco_lines(draw, COLORS["warm_white"], "story3")
    
    # Шрифты
    font_title = get_font("cormorant_regular", 82)
    font_hero = get_font("cormorant_bold", 150)
    font_subtitle = get_font("inter_medium", 64)
    font_details = get_font("inter_regular", 50)
    font_cta = get_font("inter_semibold", 54)
    
    # Композиция (с safe zones)
    y = 480
    
    # Заголовок
    draw_centered_text(draw, "Индивидуальный почерк", y, font_title, COLORS["warm_white"], STORY_SIZE[0])
    y += 100
    draw_centered_text(draw, "ар-деко", y, font_title, COLORS["warm_white"], STORY_SIZE[0])
    
    # Hero: "100 ЛЕТ"
    y += 180
    draw_centered_text(draw, "100 ЛЕТ", y, font_hero, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=25)
    
    # Тонкая линия-разделитель
    y += 200
    draw.line([(340, y), (740, y)], fill=COLORS["warm_white"], width=2)
    
    # Детали
    y += 80
    draw_centered_text(draw, "4 дня", y, font_subtitle, COLORS["warm_white"], STORY_SIZE[0])
    y += 85
    draw_centered_text(draw, "с Ольгой Розет", y, font_details, COLORS["warm_white"], STORY_SIZE[0])
    y += 65
    draw_centered_text(draw, "и Натальей Логиновой", y, font_details, COLORS["warm_white"], STORY_SIZE[0])
    
    # Условия
    y += 120
    draw_centered_text(draw, "До 12 человек", y, font_details, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=2)
    y += 70
    draw_centered_text(draw, "1 550 €", y, font_subtitle, COLORS["warm_white"], STORY_SIZE[0])
    
    # CTA блок
    y += 140
    
    # "Свайп вверх" с стрелкой
    arrow_y = y - 10
    draw.polygon([(540, arrow_y - 30), (520, arrow_y), (540, arrow_y), (540, arrow_y + 5), 
                  (560, arrow_y + 5), (560, arrow_y), (580, arrow_y), (560, arrow_y - 30)], 
                 fill=COLORS["warm_white"])
    
    y += 60
    draw_centered_text(draw, "parisinjanuary.ru", y, font_cta, COLORS["warm_white"], STORY_SIZE[0], letter_spacing=2)
    
    return img

def main():
    """Генерирует гениальные сториз"""
    print("Instagram Stories Generator v2 — Genius Edition")
    print()
    print("→ Подготовка шрифтов...")
    download_fonts()
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print()
    print("→ Генерация Stories...")
    print(f"  Размер: {STORY_SIZE[0]}x{STORY_SIZE[1]}px")
    print(f"  Выходная директория: {OUTPUT_DIR}")
    print()
    
    # Story 1
    print("  [1/3] Hook: Философский вопрос...")
    story1 = generate_story_1_genius()
    story1_path = OUTPUT_DIR / "story_1_hook_v2.png"
    story1.save(story1_path, "PNG", quality=100, optimize=True)
    
    # Story 2
    print("  [2/3] Value: Цитата куратора...")
    story2 = generate_story_2_genius()
    story2_path = OUTPUT_DIR / "story_2_value_v2.png"
    story2.save(story2_path, "PNG", quality=100, optimize=True)
    
    # Story 3
    print("  [3/3] CTA: Призыв к действию...")
    story3 = generate_story_3_genius()
    story3_path = OUTPUT_DIR / "story_3_cta_v2.png"
    story3.save(story3_path, "PNG", quality=100, optimize=True)
    
    print()
    print("✓ Гениально! 3 сториз готовы.")
    print()
    print(f"  {story1_path.name}")
    print(f"  {story2_path.name}")
    print(f"  {story3_path.name}")
    print()
    print("→ Следующий шаг:")
    print("  1. Открыть instagram_stories/ в Finder")
    print("  2. Загрузить в Instagram")
    print("  3. На Story 3: добавить Link Sticker → https://parisinjanuary.ru")
    print("  4. Опубликовать последовательно")

if __name__ == "__main__":
    main()
