import os
import requests

# Load secrets from environment (GitHub Actions)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Just test sending a basic message
message = "✅ Telegram bot test from GitHub Action successful!"

# Send message
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}
response = requests.post(url, json=payload)

# Log response for debugging
print("Status Code:", response.status_code)
print("Response:", response.text)
