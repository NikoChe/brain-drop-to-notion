# 🧠 Brain Drop to Notion

> Connect ChatGPT → Telegram → Notion. Automatically.  
> Связка ChatGPT → Telegram → Notion. Автоматически.

EN:  
**Brain Drop to Notion** is a Telegram bot running in Docker.  
It automatically saves approved ideas from ChatGPT into your Notion via a trigger phrase.

RU:  
**Brain Drop to Notion** — это Telegram-бот, работающий в Docker.  
Он сохраняет утверждённые идеи из ChatGPT в ваш Notion — по триггерной фразе.

---

## 🚀 How It Works / Как работает

EN:
1. You brainstorm in ChatGPT  
2. You confirm idea with a trigger phrase (e.g. `#save`)  
3. The bot sends data to your Notion database  
4. Fields: title, content, author, status, category, date

RU:
1. Вы работаете в ChatGPT (генерите идеи, пишете тексты)  
2. Подтверждаете идею триггерной фразой (например, `#записать`)  
3. Бот отправляет всё в базу Notion  
4. Поля: заголовок, текст, автор, статус, категория, дата

---

## 🧱 Features / Возможности

EN:
- ChatGPT → Telegram → Notion
- No manual copy-paste
- Custom trigger phrase
- Notion fields auto-filled
- Fully local & private
- Single user only
- Config via `.env`

RU:
- Перенос текста без копипаста
- Удобная фраза-триггер
- Автозаполнение всех полей
- Всё работает локально
- Один пользователь
- Простая настройка через `.env`

---

## 📦 Installation / Установка

### 1. Clone repository / Клонируйте репозиторий

```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

---

### 2. Configure `.env` / Настройте переменные окружения

macOS / Linux:

```bash
cp env.example .env
nano .env
```

Windows:

```powershell
copy env.example .env
notepad .env
```

---

### 3. Get tokens / Получите токены

**Telegram:**

- Create bot via @BotFather  
- Get your Telegram ID via @userinfobot  
- Paste both into `.env`

**Notion:**

- Go to https://www.notion.so/my-integrations  
- Create integration and copy the token  
- Share your database with the integration  
- Copy Database ID (32 characters) from URL

RU:
- Создайте бота в @BotFather  
- Получите свой ID в @userinfobot  
- Занесите всё в `.env`  
- Перейдите в Notion, создайте интеграцию  
- Расшарьте базу на неё  
- Возьмите ID базы из URL

---

### 4. Run the bot / Запуск бота

```bash
chmod +x run.sh
./run.sh
```

---

## 📒 Notion Template

### 🅰️ Option A — Duplicate Ready Template / Дубликат готовой базы

EN:  
Use our pre-configured template → duplicate it to your Notion.  
RU:  
Используйте готовый шаблон — нажмите "Duplicate" → добавьте в свой Notion.

👉 [🔗 Duplicate Template](https://www.notion.so/your-link-here)

---

### 🅱️ Option B — CSV Import / Импорт через CSV

EN:
Use file `notion_template_brain_drop.csv`.  
Go to Notion → New Page → Import → CSV → Select file.  
**Then manually change field types** in Notion:  
- `Status`: make it a Select  
- `Category`: make it a Select  
- `Date`: make it Date

RU:
Используйте файл `notion_template_brain_drop.csv`  
Зайдите в Notion → New Page → Import → CSV → выберите файл  
⚠️ После импорта поменяйте типы полей вручную:
- `Status` → Select  
- `Category` → Select  
- `Date` → Date

---

## ☁️ Hosted Bot (Optional)

EN:
Don’t want to run locally?  
Try the hosted bot — pay $1/month and get everything done for you.

RU:
Не хотите возиться с запуском?  
Просто подключите готового бота:

👉 [@BrainDropToNotion_Bot](https://t.me/BrainDropToNotion_Bot)

🔒 Ваши данные в зашифрованном виде  
📲 Настройка прямо через Telegram  
💰 $1 в месяц

---

## ⚠️ Limitations / Ограничения

EN:
- Only one user (open-source version)
- No database, no multi-user
- Manual setup required

RU:
- Только 1 пользователь
- Нет базы, подписок, админки
- Ручной запуск

---

## 👨‍💻 Author / Автор

Разработано для **NikoCheLab** — эксперименты по digital-автоматизации  
для творцов и экспертов, которые не разбираются в коде.

GitHub: [@NikoChe](https://github.com/NikoChe)  
Telegram: [@NikoChe](https://t.me/NikoChe)

---

## 📄 License / Лицензия

MIT — use it, fork it, build on top.  
MIT — используйте, форкайте, дополняйте.

---

## ⭐️ Support / Поддержка

- Star the repo  
- Share with friends  
- Try the hosted bot  
- Поддержите проект ⭐️
