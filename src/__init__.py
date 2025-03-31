import os
import requests
import logging
from datetime import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TRIGGER_PHRASE = os.getenv("TRIGGER_PHRASE", "записать")
ALLOWED_USERS = [int(uid) for uid in os.getenv("ALLOWED_USERS", "").split(",") if uid]

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loaded BOT_TOKEN: %s", BOT_TOKEN)
logger.info("TRIGGER_PHRASE: %s", TRIGGER_PHRASE)
logger.info("ALLOWED_USERS: %s", ALLOWED_USERS)

# Отправка в Notion
def send_to_notion(title: str, content: str, author: str, status="новый", category="idea"):
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
    logger.info("SENDING TO NOTION: %s", data)

    response = requests.post(url, headers=headers, json=data)
    logger.info("NOTION API STATUS: %s", response.status_code)
    logger.info("NOTION API RESPONSE: %s", response.text)

    return response

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        logger.warning("Unauthorized user tried to access: %s", user_id)
        return

    await update.message.reply_text(
        f"Бот запущен. Напиши *{TRIGGER_PHRASE}* чтобы отправить запись в Notion.",
        parse_mode="Markdown"
    )

# Обработка обычного текста
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    username = user.username or user.full_name or "Unknown"
    message = update.message.text.strip()

    logger.info("NEW MESSAGE from %s (%s): %s", username, user_id, message)

    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        logger.warning("Unauthorized user: %s", user_id)
        return

    if TRIGGER_PHRASE.lower() in message.lower():
        title = message.split("\n")[0][:100]
        content = message
        author = username

        send_to_notion(title=title, content=content, author=author)
        await update.message.reply_text("✅ Запись отправлена в Notion.")
    else:
        logger.info("TRIGGER PHRASE NOT FOUND")

if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN not set. Exiting.")
        exit(1)

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
