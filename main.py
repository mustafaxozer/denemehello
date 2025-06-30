import time
import requests

# Bot Token ve Kanal Kullanıcı Adı
TOKEN = "7892492756:AAGTGRHJppz1f073k6RItF7_KlDIjDr2q40"
CHANNEL_USERNAME = "@tarihtebuguntur"

# Gönderilecek Mesaj
MESSAGE = "hello"

# Telegram API URL
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

while True:
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": MESSAGE
    }
    response = requests.post(URL, data=payload)
    print(f"Status Code: {response.status_code}, Response: {response.text}")
    time.sleep(30)
