FROM python:3.12-slim

# metadata
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_MODULE=app.main:app \
    PORT=8000

WORKDIR /app

# system deps for building some python packages (keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app source
COPY . .

# optional: run as non-root
# RUN useradd --create-home appuser && chown -R appuser /app
# USER appuser

EXPOSE 8000

# default command, override APP_MODULE or PORT with docker run -e ...
CMD ["sh", "-c", "uvicorn ${APP_MODULE} --host 0.0.0.0 --port ${PORT}"]
