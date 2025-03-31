FROM python:3.11-slim
WORKDIR /app
COPY ./src /app/src
COPY env /app/.env
RUN pip install --no-cache-dir python-telegram-bot openai requests
CMD ["python3", "/app/src/__init__.py"]