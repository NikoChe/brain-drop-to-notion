import os
import requests
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
TRIGGER_PHRASE = os.getenv("TRIGGER_PHRASE", "записать")
ALLOWED_USERS = [int(uid) for uid in os.getenv("ALLOWED_USERS", "").split(",") if uid]

print("Loaded BOT_TOKEN:", BOT_TOKEN)
print("TRIGGER_PHRASE:", TRIGGER_PHRASE)
print("ALLOWED_USERS:", ALLOWED_USERS)

def send_to_notion(title: str, content: str, author: str, status: str = "новый", category: str = "idea"):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"database_id": os.getenv("NOTION_DATABASE_ID")},
        "properties": {
            "Title": {"title": [{"text": {"content": title[:100]}}]},
            "Content": {"rich_text": [{"text": {"content": content}}]},
            "Author": {"rich_text": [{"text": {"content": author}}]},
            "Status": {"select": {"name": status}},
            "Category": {"select": {"name": category}},
            "Date": {"date": {"start": datetime.utcnow().isoformat()}}
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print("NOTION API STATUS:", response.status_code)
    print("NOTION API RESPONSE:", response.text)
    return response

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        print(f"Unauthorized user: {user_id}")
        return
    await update.message.reply_text(f"Бот запущен. Напиши '{TRIGGER_PHRASE}' чтобы отправить запись в Notion.")

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not set. Exiting.")
        exit(1)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()