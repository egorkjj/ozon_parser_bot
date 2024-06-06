import json
from tg_bot.parsers import run_selenium
import requests
def ozon_parse(article):
    
    price = run_selenium(article)
    data = {
        "price": int(str(price[1][:-1]).replace("\u2009", "")),
        "photo": price[2],
        "price_card": int(str(price[0][:-1]).replace("\u2009", ""))
    }
    return data