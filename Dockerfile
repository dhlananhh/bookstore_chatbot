FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-input -r requirements.txt

COPY ./app ./app
COPY .env .
COPY static ./static

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
