import os
from telegram import Update
from telegram.ext import ContextTypes
from notion import save_to_notion
from utils import extract_clean_text, load_lang, categorize_message

TRIGGER_PHRASE = os.getenv("TRIGGER_PHRASE", "#notion")
ALLOWED_USERS = [int(uid) for uid in os.getenv("ALLOWED_USERS", "").split(",")]
LANG = load_lang()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = LANG["ru"]
    await update.message.reply_text(lang["welcome"])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        return

    message = update.message.text
    if TRIGGER_PHRASE not in message:
        return

    content = extract_clean_text(message, TRIGGER_PHRASE)
    category = categorize_message(content)
    save_to_notion(content, update.effective_user, category)
    lang = LANG["ru"]
    await update.message.reply_text(lang["saved"])