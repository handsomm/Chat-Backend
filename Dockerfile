FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE ChatBackend.settings

COPY . /app

RUN apt update && apt install -y libpq5
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
