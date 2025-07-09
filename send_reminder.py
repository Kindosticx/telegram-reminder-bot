import requests

TOKEN = '7732151340:AAHsfjDVhL0mRdgeHsf77r5ZiWLwfBKvzKU'
CHAT_ID = '6748468475'

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

send_message("🛡️ *Cybersecurity Reminder!*\n\nToday’s task: Practice Linux, Burp, or read OWASP.\n_Reply with 'Done' when finished._")
