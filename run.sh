#!/bin/bash

# Загрузка переменных окружения
source .env

# Проверка обязательных переменных
if [ -z "$CONTAINER_NAME" ] || [ -z "$PORT" ]; then
  echo "❌ Не заданы CONTAINER_NAME или PORT в .env"
  exit 1
fi

# Остановка предыдущего контейнера
docker rm -f $CONTAINER_NAME 2>/dev/null

# Запуск
docker run --rm -it \
  --name $CONTAINER_NAME \
  -p $PORT:$PORT \
  --env-file .env \
  braindroptonotion
