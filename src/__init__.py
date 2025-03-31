import os
import requests
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")


def send_to_notion(title: str, content: str, author: str, status: str = "новый", category: str = "idea"):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Title": {
                "title": [{"text": {"content": title[:100]}}]
            },
            "Content": {
                "rich_text": [{"text": {"content": content}}]
            },
            "Author": {
                "rich_text": [{"text": {"content": author}}]
            },
            "Status": {
                "select": {"name": status}
            },
            "Category": {
                "select": {"name": category}
            },
            "Date": {
                "date": {"start": datetime.utcnow().isoformat()}
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    return response


# Пример использования
if __name__ == "__main__":
    send_to_notion(
        title="Пример: Идея шоу",
        content="Сделать запуск продукта, который синхронизирует GPT с Notion",
        author="Niko Che"
    )