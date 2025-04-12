# 🧠 Brain Drop to Notion

> ChatGPT → Notion. Automatically. No copy-paste. No context switching.  
> ChatGPT → Notion. Автоматически. Без копипаста. Без переключений.

**Brain Drop to Notion** — это Flask-сервер, работающий в Docker.  
Он сохраняет утверждённые идеи из ChatGPT в вашу базу данных Notion — по команде прямо из чата.

---

## 🚀 Как это работает

1. Вы общаетесь с ChatGPT (например, генерируете идеи).
2. Когда идея готова, пишете  — и она уходит в Notion.
3. Flask-сервер принимает данные и сохраняет их в таблицу.
4. Telegram уведомляет вас о результате (успешно или ошибка).

---

## ⚙️ Возможности

- ✅ ChatGPT → Notion по API (без ручных действий)
- ✅ Поддержка Docker
- ✅ Минимальная конфигурация через 
- ✅ Telegram-уведомления (если включены)
- ✅ Готовые шаблоны базы данных на русском и английском

---

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/nikochelab/brain-drop-to-notion.git
cd brain-drop-to-notion
```

2. Скопируйте :
```bash
cp env.example .env
nano .env
```

3. Получите и укажите:
- Notion Token → https://www.notion.so/my-integrations
- Notion Database ID → из URL вашей базы
- Telegram Bot Token → через @BotFather (опционально)
- Telegram Chat ID → через @userinfobot (опционально)

4. Запустите бота:
```bash
chmod +x run.sh
./run.sh
```

---

## 🧠 Пример .env файла

```dotenv
BOT_TOKEN=ваш_бот_токен
ALLOWED_USERS=123456789
NOTION_TOKEN=ваш_секретный_токен
NOTION_DATABASE_ID=ваш_id_базы
PORT=9889
CONTAINER_NAME=brain-drop
```

---

## 📝 Структура базы Notion

Рекомендуется использовать готовый шаблон базы:

- 🇷🇺 [RU-шаблон](https://amused-bandicoot-285.notion.site/BrainDrop-Public-Template-RU-1c86e14c726580d48a6fc588dae1ddf3?pvs=4)
- 🇬🇧 [EN-template](https://amused-bandicoot-285.notion.site/BrainDrop-Public-Template-EN-1c86e14c7265802791d4f07e13d96fbc)

База должна содержать поля:

| Поле     | Тип      |
|----------|----------|
| Title    | Title    |
| Content  | Text     |
| Author   | Text     |
| Status   | Select   |
| Category | Select   |
| Date     | Date     |

---

## 🔌 ChatGPT интеграция

Вы можете использовать расширение в ChatGPT для автоматической отправки:

- Расширение вызывает `/new-entry`
- Структура передаваемых данных:
```json
{
  "project": "brain-drop-to-notion",
  "content": "идея или текст",
  "status": "готово",
  "category": "idea",
  "author": "Niko Che"
}
```

---

## 💬 Поддержка проекта

Если проект полезен:

- ⭐ Поставьте звезду на GitHub
- 📣 Расскажите о проекте
- 💸 Поддержите донатом → [https://nikoche.ru/donate](https://nikoche.ru/donate)
- 🔁 Или используйте готовый бот за /мес (ссылка в базе Notion)

---

Разработано для **NikoCheLab** — эксперименты по digital-автоматизации для творцов и экспертов, которые не разбираются в коде.
