FROM python:3.11-slim

WORKDIR /app
COPY ./bot /app

RUN pip install --no-cache-dir python-telegram-bot requests

CMD ["python", "main.py"]