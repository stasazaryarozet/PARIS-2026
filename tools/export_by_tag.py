#!/usr/bin/env python3
"""
Экспорт контактов по тегам для email-рассылок
Принцип q1: Без Mailchimp API, только CSV

Использование:
python3 tools/export_by_tag.py VIP          # → VIP_contacts.csv
python3 tools/export_by_tag.py Студент      # → Студент_contacts.csv
python3 tools/export_by_tag.py Коллега      # → Коллега_contacts.csv
python3 tools/export_by_tag.py all          # → all_contacts.csv (все с email)
"""

import csv
import re
from pathlib import Path
from typing import List, Dict


class EmailExporter:
    """Экспортер контактов по тегам для email-рассылок"""

    def __init__(self, address_list_path: str = "../ADDRESS_LIST.csv"):
        self.address_list_path = Path(__file__).parent.parent / "ADDRESS_LIST.csv"
        self.email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')

    def is_valid_email(self, email: str) -> bool:
        """Валидация email"""
        if not email or not isinstance(email, str):
            return False
        email = email.strip()
        if not email:
            return False
        return bool(self.email_pattern.match(email))

    def load_contacts(self) -> List[Dict]:
        """Загрузка контактов из ADDRESS_LIST.csv"""
        contacts = []
        if not self.address_list_path.exists():
            print(f"ADDRESS_LIST.csv не найден: {self.address_list_path}")
            return contacts

        with open(self.address_list_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(row)

        return contacts

    def export_by_tag(self, tag: str, output_path: str = None) -> str:
        """
        Экспорт контактов по тегу
        tag: конкретный тег или 'all' для всех контактов с email
        """
        contacts = self.load_contacts()
        if not contacts:
            print("Контакты не найдены")
            return None

        # Фильтрация по тегу
        if tag.lower() == 'all':
            filtered = [c for c in contacts if self.is_valid_email(c.get('Email', ''))]
            filename = "all_contacts.csv"
        else:
            filtered = [
                c for c in contacts
                if c.get('Tag', '').strip() == tag and self.is_valid_email(c.get('Email', ''))
            ]
            # Безопасное имя файла (заменяем пробелы и специальные символы)
            safe_tag = re.sub(r'[^\w\-_]', '_', tag)
            filename = f"{safe_tag}_contacts.csv"

        if not filtered:
            print(f"Контакты с тегом '{tag}' и валидным email не найдены")
            return None

        # Определение пути вывода
        if output_path:
            output_file = Path(output_path)
        else:
            output_file = Path(__file__).parent.parent / filename

        # Экспорт в CSV (формат для Mailchimp/Sendinblue)
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)

            # Заголовки для Mailchimp
            writer.writerow(['Email', 'First Name', 'Last Name'])

            for contact in filtered:
                email = contact.get('Email', '').strip()
                name = contact.get('Name', '').strip()

                # Разделение имени на First Name и Last Name
                name_parts = name.split()
                first_name = name_parts[0] if name_parts else ''
                last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

                writer.writerow([email, first_name, last_name])

        print(f"Экспортировано {len(filtered)} контактов в {output_file}")
        print(f"Формат: Email, First Name, Last Name (совместим с Mailchimp/Sendinblue)")

        # Статистика
        self.print_stats(filtered, tag)

        return str(output_file)

    def print_stats(self, contacts: List[Dict], tag: str):
        """Вывод статистики экспорта"""
        total = len(contacts)

        print(f"\n=== СТАТИСТИКА ЭКСПОРТА ===")
        print(f"Тег: {tag}")
        print(f"Всего контактов: {total}")

        # Домены
        domains = {}
        for contact in contacts:
            email = contact.get('Email', '')
            if '@' in email:
                domain = email.split('@')[1].lower()
                domains[domain] = domains.get(domain, 0) + 1

        print("Домены:")
        for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True):
            print(f"  {domain}: {count}")

    def list_available_tags(self):
        """Вывод доступных тегов"""
        contacts = self.load_contacts()
        tags = set()

        for contact in contacts:
            tag = contact.get('Tag', '').strip()
            if tag:
                tags.add(tag)

        if tags:
            print("Доступные теги:")
            for tag in sorted(tags):
                count = sum(1 for c in contacts if c.get('Tag', '').strip() == tag)
                email_count = sum(1 for c in contacts
                                if c.get('Tag', '').strip() == tag and self.is_valid_email(c.get('Email', '')))
                print(f"  '{tag}': {count} контактов ({email_count} с email)")
        else:
            print("Теги не найдены. Сначала нужно тегировать контакты в tagging_ui.html")

        # Также показать опцию 'all'
        total_with_email = sum(1 for c in contacts if self.is_valid_email(c.get('Email', '')))
        print(f"  'all': {total_with_email} контактов со всех тегов (только с email)")


def main():
    """Основная функция"""
    import sys

    if len(sys.argv) < 2:
        print("=== ЭКСПОРТ КОНТАКТОВ ПО ТЕГАМ ===\n")
        print("Использование:")
        print("python3 tools/export_by_tag.py <тег>")
        print("python3 tools/export_by_tag.py all    # все контакты с email")
        print("python3 tools/export_by_tag.py --list # показать доступные теги\n")

        exporter = EmailExporter()
        exporter.list_available_tags()
        return

    tag = sys.argv[1]

    if tag == '--list':
        exporter = EmailExporter()
        exporter.list_available_tags()
        return

    exporter = EmailExporter()
    output_file = exporter.export_by_tag(tag)

    if output_file:
        print(f"\n✓ Файл готов: {output_file}")
        print("Можно импортировать в Mailchimp, Sendinblue или другую систему рассылок")
    else:
        print("\n❌ Экспорт не выполнен")


if __name__ == "__main__":
    main()



