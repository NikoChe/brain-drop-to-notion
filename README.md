# 🧠 Brain Drop to Notion

> Connect ChatGPT → Telegram → Notion. Automatically. No copy-paste. No context switching.  
> Связка ChatGPT → Telegram → Notion. Автоматически. Без копипаста. Без переключений.

**Brain Drop to Notion** — это Telegram-бот, работающий в Docker, который автоматически сохраняет утверждённый текст из ChatGPT в вашу базу данных Notion.  
Достаточно добавить триггерную фразу (например, `#записать`) — и всё будет отправлено в Notion.

---

## 🚀 How It Works / Как это работает

1. You chat with ChatGPT (e.g. brainstorming, writing content).  
   Вы общаетесь с ChatGPT (например, придумываете идеи, пишете текст).

2. When the message is ready, add a trigger phrase (e.g. `#записать`).  
   Когда текст готов, добавьте триггер-фразу (например, `#записать`).

3. The Telegram bot sees the message and sends it to Notion.  
   Бот перехватывает сообщение и отправляет его в Notion.

4. The record includes title, content, author, status, category, date.  
   Запись включает заголовок, текст, автора, статус, категорию и дату.

---

## 🧱 Features / Особенности

- ✅ ChatGPT → Telegram → Notion: no manual copy/paste  
- ✅ Simple trigger phrase (`#записать`)
- ✅ Automatic field population: Title, Content, Author, Date, Status, Category
- ✅ Works fully on your side (privacy-first)
- ✅ Only one user supported (open-source version)
- ✅ Configuration via `env.example`

---

## 📦 Installation / Установка

### 1. Clone the repository / Клонируйте репозиторий:

```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

---

### 2. Copy and edit the env file / Создайте файл `.env`:

#### Linux/macOS:
```bash
cp env.example .env
nano .env
```

#### Windows:
```powershell
copy env.example .env
notepad .env
```

---

### 3. Get your credentials / Получите токены:

#### Telegram:
- Create a bot via [@BotFather](https://t.me/BotFather)
- Get your personal Telegram ID via [@userinfobot](https://t.me/userinfobot)
- Add it to `ALLOWED_USERS` in `.env`

#### Notion:
- Go to [Notion Integrations](https://www.notion.so/my-integrations)
- Create new integration → copy the token
- Share your database with the integration
- Copy the **Database ID** from the URL (32 characters)

---

### 4. Build and run the bot / Соберите и запустите бота:

```bash
chmod +x run.sh
./run.sh
```

Если вручную:
```bash
docker build -t $CONTAINER_NAME .
docker run --rm -it --name $CONTAINER_NAME -p $PORT:$PORT --env-file .env $CONTAINER_NAME
```

---

## 🧠 Example `.env` File / Пример `.env`

```env
BOT_TOKEN=your_telegram_bot_token
ALLOWED_USERS=123456789
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TRIGGER_PHRASE=#записать
DEFAULT_LANG=ru
MODE=dev
PORT=9889
CONTAINER_NAME=braindroptonotion
```

---

## 🧾 Notion Template / Шаблон Базы Notion

Используйте `notion_template_brain_drop.csv` для импорта:
- Notion → New page → Import → CSV → выберите файл

Создастся таблица с полями:
- **Title** (заголовок, max 100 символов)
- **Content** (текст)
- **Author** (имя)
- **Status** (новый / черновик / готово)
- **Category** (idea, product, task, content, general)
- **Date** (дата создания)

---

## 📥 Hosted Bot / Готовый бот

Если не хотите запускать локально — используйте уже развернутый бот:

👉 [@BrainDropToNotion_Bot](https://t.me/BrainDropToNotion_Bot) — **$1 в месяц**  
Все данные хранятся в зашифрованном виде, вы настраиваете токены через Telegram.

---

## ⚠️ Limitations / Ограничения

- Open-source версия поддерживает **только одного пользователя**
- Без базы данных, подписок, админки
- Всё запускается **локально**, вручную

---

## 👨‍💻 Author / Автор

Разработано в [NikoCheLab] — digital-автоматизация для творцов и экспертов.

- GitHub: [@nikoche](https://github.com/nikoche)
- Telegram: [@NikoChe](https://t.me/NikoChe)

---

## 📄 License / Лицензия

MIT — use it, fork it, build on top of it.  
MIT — используйте, форкайте, улучшайте.

---

## ⭐️ Support / Поддержка

Если проект был полезен:
- поставьте ⭐️ на GitHub
- поделитесь с друзьями
- оформите подписку или донат на hosted-бота

