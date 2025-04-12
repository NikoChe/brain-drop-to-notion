#!/bin/bash

source .env

if [ -z "$CONTAINER_NAME" ] || [ -z "$PORT" ]; then
  echo "❌ CONTAINER_NAME or PORT is not set in .env"
  exit 1
fi

echo "🧹 Удаляем предыдущий контейнер (если был)..."
docker rm -f $CONTAINER_NAME 2>/dev/null

echo "🐳 Сборка образа Docker..."
docker build -t $CONTAINER_NAME .

echo "🚀 Запуск контейнера $CONTAINER_NAME на порту $PORT"
docker run --rm -it --name $CONTAINER_NAME -p $PORT:$PORT --env-file .env $CONTAINER_NAME
