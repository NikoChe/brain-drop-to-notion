# 🧠 Brain Drop to Notion

> Connect ChatGPT → Telegram → Notion. Automatically. No copy-paste. No context switching.

**Brain Drop to Notion** is a lightweight Telegram bot running in a Docker container that automatically saves approved content from ChatGPT into your personal Notion database. Just add a trigger phrase (e.g. `#notion`) — and it handles the rest.

---

## 🚀 How It Works

1. You chat with ChatGPT (brainstorming ideas, writing content, etc.)
2. When the message is ready — you end it with `#notion`
3. The Telegram bot catches the message, cleans it up and sends it to Notion:
   - with date, category, author and "new" status
   - with automatic categorization by keywords

---

## 🧱 Features

- 🔗 GPT → Telegram → Notion workflow
- 🧠 Auto-categorization (idea, product, content, task)
- 🔐 Fully private: hosted by you, using your tokens
- 🌍 Multi-language: English / Russian support
- ⚙️ Configured via `.env`
- 🐳 One-click Docker launch
- 🧘 No databases, no subscriptions, no third-party APIs

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

### 2. Copy and edit `.env`

#### 🐧 macOS / Linux:

```bash
cp .env.example .env
nano .env
```

#### 🪟 Windows (PowerShell):

```powershell
Copy-Item .env.example .env
notepad .env
```

### 3. Get your tokens

- Create a bot via `@BotFather` on Telegram
- Generate Notion integration token at https://notion.so/my-integrations
- Share your database with the integration
- Extract your `NOTION_DATABASE_ID` from the database URL

### 4. Run the bot

```bash
docker build -t brain-drop .
docker run --name $CONTAINER_NAME --env-file .env -p $PORT:$PORT brain-drop
```

---

## 🧠 .env Example

```env
# Telegram
TELEGRAM_BOT_TOKEN=your_telegram_token_here
ALLOWED_USERS=123456789

# Notion
NOTION_TOKEN=your_notion_integration_token_here
NOTION_DATABASE_ID=your_database_id_here

# Behavior
TRIGGER_PHRASE=#notion

# Docker
PORT=9889
CONTAINER_NAME=brain-drop-to-notion-container
```

---

## ⚠️ Limitations

This open-source version:
- Supports one user only

---

## 🔗 Don’t want to host it?

Try the **hosted version** at  
👉 [t.me/BrainDropToNotion_Bot](https://t.me/BrainDropToNotion_Bot) — just **$1/month**

- Connect your keys via Telegram
- Data is stored encrypted
- Works instantly without Docker

---

## 👨‍💻 Author

Created by [NikoCheLab] — building digital automations at the edge of creativity and productivity.

- GitHub: [@nikoche](https://github.com/nikoche)
- Telegram: [@NikoChe](https://t.me/NikoChe)

---

## 🧾 License

MIT — use it, fork it, improve it.

---

# 🧠 Brain Drop to Notion (РУССКИЙ)

> Связка ChatGPT → Telegram → Notion. Автоматически. Без копипаста. Без переключений.

**Brain Drop to Notion** — это Telegram-бот, работающий в Docker, который позволяет автоматически передавать утверждённый контент из чата с ChatGPT прямо в ваш Notion.

---

## 🚀 Как это работает

1. Вы общаетесь с ChatGPT (например, пишете пост, стратегию, идею).
2. Когда текст готов — в конце добавляете `#notion`
3. Telegram-бот принимает это сообщение, очищает и сохраняет его в вашу базу в Notion:
   - с датой, категорией, статусом и автором
   - с автокатегоризацией по ключевым словам

---

## 🧱 Особенности

- 🔗 Связка GPT → Telegram → Notion
- 🧠 Автокатегоризация (idea, product, content, task)
- 🔐 Приватно: всё работает у вас, без сторонних API
- 🌍 Мультиязычность (RU / EN)
- ⚙️ Простая настройка через `.env`
- 🐳 Запуск в один клик через Docker

---

## 📦 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

2. Создайте и настройте `.env`:

#### 🐧 macOS / Linux:

```bash
cp .env.example .env
nano .env
```

#### 🪟 Windows (PowerShell):

```powershell
Copy-Item .env.example .env
notepad .env
```

3. Получите токены:
- Создайте бота через `@BotFather` в Telegram
- Получите Notion токен на [notion.so/my-integrations](https://notion.so/my-integrations)
- Поделитесь базой с интеграцией
- Извлеките `DATABASE_ID` из URL

4. Запустите:

```bash
docker build -t brain-drop .
docker run --name $CONTAINER_NAME --env-file .env -p $PORT:$PORT brain-drop
```

---

## 🧠 Пример `.env`

```env
TELEGRAM_BOT_TOKEN=your_telegram_token_here
ALLOWED_USERS=123456789
NOTION_TOKEN=your_notion_integration_token_here
NOTION_DATABASE_ID=your_database_id_here
TRIGGER_PHRASE=#notion
PORT=9889
CONTAINER_NAME=brain-drop-to-notion-container
```

---

## ⚠️ Ограничения

**Open-source версия**:
- Только для одного пользователя

---

## 🔗 Хочешь не разворачивать?

Подключайся к **готовому боту**:  
👉 [t.me/BrainDropToNotion_Bot](https://t.me/BrainDropToNotion_Bot) — всего **$1 в месяц**

- Вводишь ключи через Telegram
- Всё хранится зашифрованно
- Никакого VPS и Docker

---

## 👨‍💻 Автор

Проект — часть практики “Автоматизируй свою голову”  
Лаборатория: [NikoCheLab]

- GitHub: [@nikoche](https://github.com/nikoche)
- Telegram: [@NikoChe](https://t.me/NikoChe)

---

## 🧾 Лицензия

MIT — используй, адаптируй, распространяй.