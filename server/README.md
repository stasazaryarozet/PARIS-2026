# Paris‑2026 — Self‑Hosted Form API

Минимальный сервер для приёма заявок без сторонних провайдеров.

## Быстрый старт (локально)

```bash
cd server
cp .env.example .env   # создайте файл окружения
docker compose up -d --build

# Проверка
curl -s http://localhost:8000/health
```

## Конфигурация

- `FORM_EMAIL_TO` — куда отправлять заявки
- `FORM_EMAIL_FROM` — адрес-отправитель домена
- `SMTP_*` — настройки SMTP
- `SALT` — соль для хэширования IP
- `ALLOWED_ORIGINS` — допустимые Origin (CORS)

## Endpoint

`POST /api/submit` — принимает поля формы `name`, `contact`, `consent` и скрытое `_honey`.

Ответ: `{ "ok": true }` при успехе. Ошибки: 400/429/500.

## Логи

Файл `server/data/submissions.log` (ротация вне контейнера).








