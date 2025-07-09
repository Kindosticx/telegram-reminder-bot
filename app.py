from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

TOKEN = '7732151340:AAHsfjDVhL0mRdgeHsf77r5ZiWLwfBKvzKU'
CHAT_ID = '6748468475'
LOG_FILE = "progress_log.txt"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        text = data["message"]["text"].strip().lower()
        if text == "/start":
            send_message("👋 Welcome! You’ll get daily study reminders. Reply with 'Done' after studying.")
        elif text == "done":
            with open(LOG_FILE, "a") as f:
                f.write(f"{datetime.now()} - Done\n")
            send_message("✅ *Progress recorded!* Keep going.")
    return "", 200

@app.route("/log")
def get_log():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.read()
        return f"<pre>{logs}</pre>"
    except FileNotFoundError:
        return "No logs found."
