from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import re, smtplib, ssl, json, time, hashlib, os
from typing import Optional

# Google Sheets
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = FastAPI()

ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "https://parisinjanuary.ru,http://localhost:8000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST"],
    allow_headers=["*"],
)

EMAIL_TO = os.environ.get("FORM_EMAIL_TO", "info@parisinjanuary.ru")
EMAIL_FROM = os.environ.get("FORM_EMAIL_FROM", "no-reply@parisinjanuary.ru")
SMTP_HOST = os.environ.get("SMTP_HOST", "mail.parisinjanuary.ru")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")
SALT = os.environ.get("SALT", "")

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
PHONE_RE = re.compile(r"^[\d\s\-\+\(\)]{7,}$")


def valid_contact(s: str) -> bool:
    return bool(EMAIL_RE.match(s) or PHONE_RE.match(s))


def log_submission(payload: dict, ip: str):
    rec = {
        "t": int(time.time()),
        "ip": hashlib.sha256((ip + SALT).encode()).hexdigest(),
        "data": payload,
    }
    with open("/app/submissions.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def send_email(subject: str, body: str):
    ctx = ssl.create_default_context()
    msg = (
        f"From: {EMAIL_FROM}\r\nTo: {EMAIL_TO}\r\nSubject: {subject}\r\n"
        f"Content-Type: text/plain; charset=utf-8\r\n\r\n{body}"
    )
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls(context=ctx)
        if SMTP_USER and SMTP_PASS:
            s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(EMAIL_FROM, [EMAIL_TO], msg.encode("utf-8"))


def append_to_sheet(name: str, contact: str, when_ts: int):
    spreadsheet_id = os.environ.get("GSHEET_ID")
    sheet_name = os.environ.get("GSHEET_SHEET", "Submissions")
    credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not spreadsheet_id or not credentials_json:
        return  # silently skip if not configured
    creds = service_account.Credentials.from_service_account_info(
        json.loads(credentials_json), scopes=[
            "https://www.googleapis.com/auth/spreadsheets"
        ]
    )
    service = build("sheets", "v4", credentials=creds, cache_discovery=False)
    values = [[time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(when_ts)), name, contact]]
    body = {"values": values}
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A:C",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()


@app.post("/api/submit")
async def submit(
    request: Request,
    name: str = Form(...),
    contact: str = Form(...),
    consent: str = Form(...),
    _honey: str = Form(""),
    _tstart: str = Form("")
):
    if _honey:
        raise HTTPException(status_code=400, detail="bot")
    if not name or not valid_contact(contact) or not consent:
        raise HTTPException(status_code=400, detail="invalid")
    # simple timing check (>= 2s)
    try:
        tstart = int(_tstart)
        if time.time() - (tstart/1000.0) < 2:
            raise HTTPException(status_code=400, detail="bot-fast")
    except Exception:
        pass

    ip = request.client.host if request.client else "0.0.0.0"
    payload = {"name": name.strip(), "contact": contact.strip()}
    log_submission(payload, ip)
    ts = int(time.time())
    try:
        send_email("Париж январь 2026 — заявка", f"Имя: {name}\nКонтакт: {contact}\n")
    except Exception:
        # всё равно возвращаем ok, чтобы не раскрывать внутренние детали
        pass
    try:
        append_to_sheet(name, contact, ts)
    except Exception:
        pass
    return {"ok": True}


@app.get("/health")
async def health():
    return {"ok": True}


