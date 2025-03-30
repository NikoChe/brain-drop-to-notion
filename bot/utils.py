import json
from pathlib import Path

def extract_clean_text(text, trigger):
    return text.replace(trigger, "").strip()

def load_lang():
    with open(Path(__file__).parent / "lang.json", "r", encoding="utf-8") as f:
        return json.load(f)

def categorize_message(text):
    keywords = {
        "product": ["бот", "сервис", "продукт", "репа"],
        "content": ["пост", "видео", "цитата", "контент"],
        "idea": ["идея", "мысля", "вдохновение"],
        "task": ["сделать", "собрать", "проверить"],
    }
    for category, keys in keywords.items():
        if any(k in text.lower() for k in keys):
            return category
    return "general"