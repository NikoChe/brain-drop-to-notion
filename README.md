# Brain Drop to Notion

**Brain Drop to Notion (BDTN)** — это Telegram-бот, работающий в Docker-контейнере, который позволяет сохранять структурированный контент из Telegram в ваш личный Notion.

## Возможности
- Сохранение мыслей, текстов, заметок и идей по триггер-фразе
- Указание категории, типа контента, статуса, даты и автора
- Интеграция с Notion API
- Установка и запуск в один клик через Docker

## Установка

### 1. Клонируй репозиторий:
```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

### 2. Создай `.env` файл на основе `.env.example`

### 3. Запусти через Docker:
```bash
docker-compose up -d
```

## Переменные окружения

Все переменные описаны в `.env.example`.

## Лицензия
MIT---

## 🌍 Description / Описание

### 🇬🇧 English
**Brain Drop to Notion** is a simple yet powerful Telegram bot that lets you instantly save any approved messages, ideas, or notes from Telegram into your personal Notion workspace.  
Runs in a Docker container, configured via `.env`, and deploys in seconds.  
Fully private. Install locally or on your VPS.  
⚙️ Flow: type → trigger → content saved to Notion  
🚀 Fully customizable: categories, types, statuses, tags

### 🇷🇺 Русский
**Brain Drop to Notion** — это простой, но мощный Telegram-бот, который позволяет сохранять любые утверждённые тексты, идеи и заметки из Telegram прямо в ваш Notion.  
Работает в Docker-контейнере, настраивается через `.env`, и запускается в пару кликов.  
Полностью приватный. Устанавливается локально или на VPS.  
⚙️ Сценарий: пишешь → ставишь триггер-фразу → контент уходит в твой Notion  
🚀 Можно кастомизировать под себя: категории, типы, статусы, теги

---

## 🤖 Welcome Message / Приветствие

### 🇬🇧 English
```
Hi there! 👋

I’m BrainDropToNotion_Bot — here to help you save your thoughts, ideas, and notes into your personal Notion space.

🔹 Just send me a message with the trigger phrase (default: #notion)  
🔹 I’ll push it into your Notion database  
🔹 I’ll add date, category, author and status

Need help? Type /help  
Example: "Brilliant automation idea #notion"
```

### 🇷🇺 Русский
```
Привет! 👋

Я — BrainDropToNotion_Bot.  
Моя задача — сохранять твои идеи, мысли и тексты в твой личный Notion.

🔹 Напиши сообщение с триггер-фразой (по умолчанию: #notion)  
🔹 Я отправлю его в твою базу данных  
🔹 Укажу дату, категорию, автора и статус

Команда помощи: /help  
Пример: "Гениальная мысль про автоматизацию #notion"
```