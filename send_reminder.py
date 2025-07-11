import json
import requests
import os
import random
from datetime import datetime

# 🔐 Load from GitHub Secrets
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# 🧪 Debug prints — remove later when confirmed working
print("Token:", TELEGRAM_TOKEN)
print("Chat ID:", CHAT_ID)

# 🎯 Motivational quotes
quotes = [
    "Keep going — you're building something powerful 💪",
    "You’re not behind — you’re becoming 🔐",
    "Every day of effort brings you closer 🔍",
    "Stay consistent — greatness compounds 🛡",
    "You’ve got what it takes, stay locked in 🚀"
]
quote = random.choice(quotes)

# 📖 Load progress
with open("progress.json", "r") as f:
    progress = json.load(f)
current_day = progress["current_day"]

# 📅 Load 12-week roadmap
with open("roadmap.json", "r") as f:
    roadmap = json.load(f)["days"]

# 🛠 Build message
if current_day > len(roadmap):
    message = "🎉 You’ve completed the 12-week penetration testing roadmap!"
else:
    day = roadmap[current_day - 1]
    message = f"""🛡️ *{day['title']}*

📝 Task: {day['task']}
📺 [Watch Video]({day['video']})
🧪 [Try Lab]({day['lab']})

📅 {day['date']} | Day {current_day}/84  
✨ _{quote}_"""

# 📤 Send to Telegram
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}
response = requests.post(url, json=payload)

# 🧪 Print Telegram response for debugging
print("Status Code:", response.status_code)
print("Response:", response.text)

# 🔁 Update Progress
if current_day <= len(roadmap):
    progress["current_day"] += 1
    with open("progress.json", "w") as f:
        json.dump(progress, f)
