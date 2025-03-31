#!/bin/bash
source .env
if [ -z "$CONTAINER_NAME" ] || [ -z "$PORT" ]; then
  echo "❌ CONTAINER_NAME or PORT is not set in env"
  exit 1
fi
docker rm -f $CONTAINER_NAME 2>/dev/null
docker build -t $CONTAINER_NAME .
docker run --rm -it --name $CONTAINER_NAME -p $PORT:$PORT --env-file .env $CONTAINER_NAME
