import os
import requests
from datetime import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
TRIGGER_PHRASE = os.getenv("TRIGGER_PHRASE", "#забираем")
DEFAULT_AUTHOR = os.getenv("DEFAULT_AUTHOR", "ChatGPT")
DEFAULT_STATUS = "черновик"

app = Flask(__name__)

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

@app.route("/new-entry", methods=["POST"])
def new_entry():
    data = request.get_json()

    print("📥 Получены данные:", data)

    content = data.get("content", "").strip()
    if TRIGGER_PHRASE.lower() not in content.lower():
        print("⛔️ Триггерная фраза не найдена. Запись не отправлена.")
        return jsonify({"error": "trigger not found"}), 400

    project = data.get("project", "Untitled Project")
    author = data.get("author", DEFAULT_AUTHOR)
    status = data.get("status", DEFAULT_STATUS)
    category = data.get("category", "idea")

    title = f"{project} — {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    print("📄 Формируем запись с заголовком:", title)

    notion_payload = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": title}}]},
            "Content": {"rich_text": [{"text": {"content": content}}]},
            "Author": {"rich_text": [{"text": {"content": author}}]},
            "Status": {"select": {"name": status}},
            "Category": {"select": {"name": category}},
            "Date": {"date": {"start": datetime.now().isoformat()}}
        }
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=notion_payload)

    print("📬 Ответ от Notion:")
    print("Status:", response.status_code)
    print("Text:", response.text)

    if response.status_code == 200:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"error": "failed to create entry"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", "9889"))
    print(f"🚀 Flask-сервер запущен на порту {port}")
    app.run(host="0.0.0.0", port=port)
