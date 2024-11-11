import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(chat_id, message):
    """Отправляет сообщение в телеграм"""

    params = {"text": message, "chat_id": chat_id}
    url = f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage"
    # print(url)
    requests.get(url, params=params)