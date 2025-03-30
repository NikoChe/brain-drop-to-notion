import os
import requests
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def save_to_notion(text, user, category="general"):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Title": {
                "title": [{ "text": { "content": text[:100] } }]
            },
            "Content": {
                "rich_text": [{ "text": { "content": text } }]
            },
            "Author": {
                "rich_text": [{ "text": { "content": user.full_name } }]
            },
            "Status": {
                "select": { "name": "новый" }
            },
            "Category": {
                "select": { "name": category }
            },
            "Date": {
                "date": { "start": datetime.utcnow().isoformat() }
            }
        }
    }
    requests.post(url, headers=headers, json=data)