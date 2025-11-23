#!/bin/bash

# Если папка alembic существует, накатываем миграции
if [ -d "alembic" ]; then
    alembic upgrade head
fi

# Запускаем сервер (с авто-перезагрузкой для разработки)
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
