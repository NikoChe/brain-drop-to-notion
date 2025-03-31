FROM python:3.11-slim
WORKDIR /app
COPY ./src /app/src
<<<<<<< HEAD
COPY env /app/.env
RUN pip install --no-cache-dir python-telegram-bot openai requests
CMD ["python3", "/app/src/__init__.py"]
=======
COPY .env /app/.env
RUN pip install --no-cache-dir python-telegram-bot openai requests
CMD ["python3", "/app/src/__init__.py"]
>>>>>>> 0dc1e07a38acef08a6f6c2f78344d014f35a5330
