import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(transaction):
    """Получение суммы платежа в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    params = {"to": "RUB", "from": transaction["operationAmount"]["currency"]["code"], "amount": amount}
    headers = {"apikey": API_KEY}
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(amount)
    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert?", params=params, headers=headers
        )
        recived_data = response.json()
        return float(recived_data["result"])
    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert?", params=params, headers=headers
        )
        recived_data = response.json()
        return float(recived_data["result"])
