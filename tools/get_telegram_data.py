#!/usr/bin/env python3
"""
Утилита для доступа к данным Telegram Bot группы "N, O, S"
Автоматически находит данные в различных возможных расположениях
"""
from pathlib import Path
import json
import os
from typing import Optional, List, Dict


class TelegramDataAccess:
    """Доступ к данным Telegram Bot группы N, O, S"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.possible_sources = [
            # Репозиторий Telegram Bot
            Path.home() / "Дела" / "Telegram Bot" / "data" / "chats" / "N_O_S",
            # Системное хранилище
            *list(Path.home().glob("TelegramArchive/*_N_O_S")),
            *list(Path.home().glob("TelegramArchive/*N_O_S*")),
            # Локальная ссылка в проекте
            self.project_root / "source_materials" / "telegram_N_O_S",
        ]
    
    def find_data_source(self) -> Optional[Path]:
        """Найти источник данных группы N, O, S"""
        for source in self.possible_sources:
            if source.exists() and source.is_dir():
                # Если это символическая ссылка, разрешаем её
                if source.is_symlink():
                    resolved = source.resolve()
                    if resolved.exists():
                        return resolved
                else:
                    return source
        return None
    
    def get_messages(self) -> List[Dict]:
        """Получить все сообщения из группы"""
        source = self.find_data_source()
        if not source:
            return []
        
        messages_file = source / "messages" / "index.json"
        if messages_file.exists():
            with open(messages_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Альтернативный формат: отдельные файлы сообщений
        messages_dir = source / "messages" / "text"
        if messages_dir.exists():
            messages = []
            for msg_file in sorted(messages_dir.glob("*.json")):
                with open(msg_file, 'r', encoding='utf-8') as f:
                    messages.append(json.load(f))
            return messages
        
        return []
    
    def get_voice_files(self) -> List[Path]:
        """Получить список голосовых файлов"""
        source = self.find_data_source()
        if not source:
            return []
        
        voice_dir = source / "voice"
        if voice_dir.exists():
            return list(voice_dir.glob("*.ogg")) + list(voice_dir.glob("*.m4a")) + list(voice_dir.glob("*.mp3"))
        
        return []
    
    def get_photos(self) -> List[Path]:
        """Получить список фотографий"""
        source = self.find_data_source()
        if not source:
            return []
        
        photos_dir = source / "photos"
        if photos_dir.exists():
            return list(photos_dir.glob("*.jpg")) + list(photos_dir.glob("*.png"))
        
        return []
    
    def get_metadata(self) -> Optional[Dict]:
        """Получить метаданные группы"""
        source = self.find_data_source()
        if not source:
            return None
        
        metadata_file = source / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def search_messages(self, query: str, from_user: Optional[str] = None) -> List[Dict]:
        """Поиск сообщений по тексту"""
        messages = self.get_messages()
        results = []
        query_lower = query.lower()
        
        for msg in messages:
            text = msg.get('text', '').lower()
            if query_lower in text:
                if from_user is None or msg.get('from', '').lower() == from_user.lower():
                    results.append(msg)
        
        return results


def main():
    """CLI для доступа к данным"""
    import sys
    
    access = TelegramDataAccess()
    source = access.find_data_source()
    
    if not source:
        print("❌ Данные группы N, O, S не найдены")
        print("\nПроверьте расположение в:")
        for src in access.possible_sources:
            print(f"  - {src}")
        print("\nИли запустите: tools/sync_telegram_data.sh")
        sys.exit(1)
    
    print(f"✅ Источник данных: {source}")
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "messages":
            messages = access.get_messages()
            print(f"\n📨 Найдено сообщений: {len(messages)}")
            for msg in messages[:10]:  # Показываем первые 10
                print(f"  {msg.get('from', 'Unknown')}: {msg.get('text', '')[:100]}")
        
        elif command == "voice":
            voice_files = access.get_voice_files()
            print(f"\n🎤 Найдено голосовых: {len(voice_files)}")
            for vf in voice_files:
                print(f"  - {vf.name}")
        
        elif command == "photos":
            photos = access.get_photos()
            print(f"\n📷 Найдено фото: {len(photos)}")
            for photo in photos:
                print(f"  - {photo.name}")
        
        elif command == "metadata":
            metadata = access.get_metadata()
            if metadata:
                print("\n📊 Метаданные:")
                print(json.dumps(metadata, indent=2, ensure_ascii=False))
            else:
                print("❌ Метаданные не найдены")
        
        elif command == "search":
            if len(sys.argv) < 3:
                print("Использование: python get_telegram_data.py search <запрос> [от_пользователя]")
                sys.exit(1)
            query = sys.argv[2]
            from_user = sys.argv[3] if len(sys.argv) > 3 else None
            results = access.search_messages(query, from_user)
            print(f"\n🔍 Найдено сообщений: {len(results)}")
            for msg in results:
                print(f"  {msg.get('from', 'Unknown')}: {msg.get('text', '')}")
        
        else:
            print(f"Неизвестная команда: {command}")
            print("Доступные команды: messages, voice, photos, metadata, search")
    else:
        metadata = access.get_metadata()
        messages = access.get_messages()
        voice_files = access.get_voice_files()
        photos = access.get_photos()
        
        print("\n📊 Статистика:")
        print(f"  Сообщений: {len(messages)}")
        print(f"  Голосовых: {len(voice_files)}")
        print(f"  Фото: {len(photos)}")
        if metadata:
            print(f"  Участников: {len(metadata.get('participants', []))}")


if __name__ == "__main__":
    main()
