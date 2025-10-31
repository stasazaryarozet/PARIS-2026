# Уведомление для основного ИИ‑разработчика

Тема: устранение зависимости формы бронирования от стороннего провайдера (Formspree) — архитектурное решение и план внедрения.

Дата: 2025‑10‑28

## Цель

- Исключить внешнего SaaS‑провайдера при приёме заявок.
- Сохранить текущий UX/UI (валидация, модальное «Спасибо»), конфиденциальность и устойчивость.
- Минимизировать инфраструктуру, энергопотребление и стоимость.

## Архитектура (самостоятельная, минимальная)

- Компонент: тонкий API‑endpoint `POST /api/submit` под доменом `api.parisinjanuary.ru` (тот же владелец домена).
- Технология: любой малый VPS (например, 1 vCPU / 512–1 GB), Docker + Caddy (TLS), Python FastAPI + uvicorn.
- Доставка: SMTP через собственный почтовый ящик домена (не SaaS), + файловое логирование заявок (JSON‑строки) на диске сервера.
- Защита: hCaptcha/turnstile (без аккаунта можно включить «moderate» режим), server‑side rate‑limit.
- Приватность: поля минимальные (имя, контакт, согласие), IP хэшируется (SHA‑256 с солью), логи крутятся и автоматически удаляются через 30 дней.

### Google Sheets (по просьбе заказчика)

- Запись каждой заявки в Google‑Таблицу (таблица в аккаунте Ольги).
- Доступ через сервисный аккаунт Google (минимальные права: только редактирование указанной таблицы).
- Секреты не храним в файлах: JSON ключ сервисного аккаунта передаётся через переменную окружения `GOOGLE_APPLICATION_CREDENTIALS_JSON` (base64 или «сырое» JSON).

### Контракт API

`POST /api/submit`  (Content‑Type: multipart/form‑data или application/json)

Request поля:
- `name` (string, 1..200)
- `contact` (string, 3..200) — email или телефон
- `consent` ("on"|true)

Response:
```json
{ "ok": true }
```
HTTP‑коды: 200 (ok), 400 (валидация), 429 (rate‑limit), 500 (ошибка).

### Безопасность
- CORS: `Origin: https://parisinjanuary.ru`
- Rate‑limit: 5 req / 10 мин / IP
- Валидация email/телефона сервером.
- Анти‑спам: скрытое поле `_honey` + таймер на клиенте + server‑side проверка времени заполнения.

## Минимальная реализация (FastAPI)

```python
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import re, smtplib, ssl, json, time, hashlib, os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["https://parisinjanuary.ru"], allow_methods=["POST"], allow_headers=["*"])

EMAIL_TO = os.environ.get("FORM_EMAIL_TO", "info@parisinjanuary.ru")
EMAIL_FROM = os.environ.get("FORM_EMAIL_FROM", "no-reply@parisinjanuary.ru")
SMTP_HOST = os.environ.get("SMTP_HOST", "mail.parisinjanuary.ru")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
PHONE_RE = re.compile(r"^[\d\s\-\+\(\)]{7,}$")

def valid_contact(s: str) -> bool:
    return bool(EMAIL_RE.match(s) or PHONE_RE.match(s))

def log_submission(payload: dict, ip: str):
    rec = {
        "t": int(time.time()),
        "ip": hashlib.sha256((ip + os.environ.get("SALT", "")).encode()).hexdigest(),
        "data": payload,
    }
    with open("submissions.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def send_email(subject: str, body: str):
    ctx = ssl.create_default_context()
    msg = f"From: {EMAIL_FROM}\r\nTo: {EMAIL_TO}\r\nSubject: {subject}\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n{body}"
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls(context=ctx)
        if SMTP_USER and SMTP_PASS:
            s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(EMAIL_FROM, [EMAIL_TO], msg.encode("utf-8"))

@app.post("/api/submit")
async def submit(request: Request, name: str = Form(...), contact: str = Form(...), consent: str = Form(...)):
    if not name or not valid_contact(contact) or not consent:
        raise HTTPException(status_code=400, detail="invalid")
    ip = request.client.host if request.client else "0.0.0.0"
    payload = {"name": name.strip(), "contact": contact.strip()}
    log_submission(payload, ip)
    send_email("Париж январь 2026 — заявка", f"Имя: {name}\nКонтакт: {contact}\n")
    append_to_sheet(name, contact, int(time.time()))
    return {"ok": True}
```

## Внедрение (этапы)

1) Инфраструктура (без Docker):
   - Поддомен `api.parisinjanuary.ru` (A/AAAA на VPS, или CNAME → reverse‑proxy).
   - Caddy/Nginx: TLS и reverse‑proxy на uvicorn (systemd‑служба).
   - Секреты окружения: `SMTP_*`, `FORM_EMAIL_TO`, `SALT`, `GSHEET_ID`, `GSHEET_SHEET`, `GOOGLE_APPLICATION_CREDENTIALS_JSON`.

2) Деплой (systemd):
   - `python3 -m venv .venv && source .venv/bin/activate && pip install -r server/requirements.txt`
   - systemd unit для uvicorn: `ExecStart=/path/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000`

3) Клиент (после запуска API):
   - В `index.html` заменить `action` формы на `/api/submit` (уже предусмотрено контрактом).
   - Оставить существующую клиентскую валидацию и модалку «Спасибо».

4) Экология/минимизация:
   - Один контейнер, ~20–30MB RAM в простое; отключённые логи uvicorn; ротация файлов‑логов.
   - Полная независимость от SaaS; вся почта — через собственный SMTP домена.

## Обратная совместимость

- Пока API не развёрнут, менять фронтенд не будем.
- После запуска эндпоинта — одно изменение: `action="/api/submit"` и удаление скрытых полей Formspree.

## Контрольный список

- [ ] Выделить малый VPS, выписать почтовые реквизиты домена
- [ ] Развернуть контейнер с FastAPI + Caddy (TLS)
- [ ] Прописать DNS для `api.parisinjanuary.ru`
- [ ] Протестировать `POST /api/submit` из браузера (CORS)
- [ ] Переключить форму на новый endpoint
- [ ] Наблюдение: почта доходит, лог записывается, rate‑limit срабатывает
- [ ] Проверить запись в Google‑Таблицу (новая строка при заявке)

## Журнал действий (агент)

- v1: Добавил FastAPI API + почта + логирование; подготовил контракт и инструкции.
- v2: Добавил интеграцию Google Sheets (через сервисный аккаунт), переменные окружения и non‑Docker запуск.

### v3: Доступы для Google Sheets и API‑домена (требуется шаг владельца)

Технически я не могу «сам» создать/получить ваши учётные данные Google и внести DNS‑записи домена без прав владельца. Подготовил точные команды/шаги — их нужно выполнить один раз (2–3 минуты):

1) Google Sheets — сервисный аккаунт

```bash
# 1. Создать сервисный аккаунт и ключ (в GCP Console или gcloud)
gcloud iam service-accounts create paris2026-forms --display-name="Paris 2026 Forms"
gcloud projects add-iam-policy-binding <GCP_PROJECT_ID> \
  --member="serviceAccount:paris2026-forms@<GCP_PROJECT_ID>.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
gcloud services enable sheets.googleapis.com
gcloud iam service-accounts keys create key.json \
  --iam-account=paris2026-forms@<GCP_PROJECT_ID>.iam.gserviceaccount.com

# 2. Открыть key.json и скопировать сырое содержимое в переменную окружения на сервере
export GOOGLE_APPLICATION_CREDENTIALS_JSON='{"type":"service_account", ...}'

# 3. В самой Google‑Таблице → Поделиться → Добавить email сервисного аккаунта
#    paris2026-forms@<GCP_PROJECT_ID>.iam.gserviceaccount.com со статусом «Редактор»

# 4. На сервере задать переменные окружения (пример)
export GSHEET_ID='<ID_таблицы_из_URL>'
export GSHEET_SHEET='Submissions'
export FORM_EMAIL_TO='info@parisinjanuary.ru'
export FORM_EMAIL_FROM='no-reply@parisinjanuary.ru'
export SMTP_HOST='mail.parisinjanuary.ru'
export SMTP_PORT='587'
export SMTP_USER='' ; export SMTP_PASS=''
export SALT='change-me'
export ALLOWED_ORIGINS='https://parisinjanuary.ru'

# 5. Перезапустить uvicorn (systemd)
sudo systemctl restart paris2026-api.service
```

2) API домен `api.parisinjanuary.ru`

```
DNS: A/AAAA → IP сервера
Reverse‑proxy (Caddy/Nginx): TLS и проксирование на 127.0.0.1:8000
Проверка: curl -sI https://api.parisinjanuary.ru/health → HTTP/2 200
```

После выполнения шагов — фронтенд уже отправляет на `https://api.parisinjanuary.ru/api/submit`; заявка должна появиться в таблице (A: время, B: имя, C: контакт). Я продолжу мониторинг и зафиксирую результат здесь.

—

Готов выполнить развёртывание и внести минимальные изменения клиента после появления `api.parisinjanuary.ru`.


