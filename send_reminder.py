import requests
from datetime import datetime
import random

TOKEN = '7732151340:AAHsfjDVhL0mRdgeHsf77r5ZiWLwfBKvzKU'
CHAT_ID = '6748468475'

quotes = [
    "Keep going — you're building something powerful 💪",
    "You’re not behind — you’re becoming 🔐",
    "Every day of effort brings you closer 🔍",
    "Stay consistent — greatness compounds 🛡️",
    "You’ve got what it takes, stay locked in 🚀"
]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
quote = random.choice(quotes)

message = f"""🛡️ *Cybersecurity Reminder!*
Today’s task: Practice Linux, Burp, or review OWASP.

🕒 Sent: `{now}`

_{quote}_

Reply with *Done* when you're done ✅
"""

send_message(message)
