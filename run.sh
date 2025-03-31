#!/bin/bash
<<<<<<< HEAD
source ./env
if [ -z "$CONTAINER_NAME" ] || [ -z "$PORT" ]; then
  echo "❌ CONTAINER_NAME or PORT is not set in env"
  exit 1
fi
docker rm -f $CONTAINER_NAME 2>/dev/null
docker build -t $CONTAINER_NAME .
docker run --rm -it --name $CONTAINER_NAME -p $PORT:$PORT --env-file env $CONTAINER_NAME
=======

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
>>>>>>> 0dc1e07a38acef08a6f6c2f78344d014f35a5330
