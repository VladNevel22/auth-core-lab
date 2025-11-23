FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# скрипт запуска
RUN echo '#!/bin/bash\nalembic upgrade head\nuvicorn src.main:app --host 0.0.0.0 --port 8000' > start.sh
RUN chmod +x start.sh

CMD ["./start.sh"]
