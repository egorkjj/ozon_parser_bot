import requests
import json
from tg_bot.parsers import run_selenium

def ozon_parse(article):
    js = {"login": "sellerY7PJZ", "password": "lhR14rkD"}
    response = requests.post(url="https://mpsklad.io/login", json=js)
    response_data = json.loads(response.text)

    price = requests.get(
        url=f"https://mpsklad.io/api/oz/get/item/{article}",
        headers={"Cookie": f"auth={response_data['message']}"},
    )

    price_data = json.loads(price.text)
    oz_card_price = run_selenium(article)
    data = {
        "price": price_data["item"]["final_price"],
        "photo": price_data["item"]["photo"],
        "name": price_data["item"]["name"],
        "price_card": oz_card_price
    }
    return data



