#!/bin/bash
docker build -t brain-drop .
docker run --name "$CONTAINER_NAME" --env-file .env -p $PORT:$PORT brain-drop