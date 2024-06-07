from aiogram import Bot
from tg_bot.DBSM import fetchall, change_price
from tg_bot.parsers import ozon_parse
import asyncio
import time

async def main():
    bot = Bot(token = '7421677549:AAGHL5x8EWp3QhWQI1CdKVF1U2cOaDmxPRQ')
    while True:
        data = fetchall()
        for i in data:
            chat_id = i.user_id
            oz_price = int(i.card_price)
            price = int(i.price)
            article = i.article
            while True:
                try:
                    data_w = ozon_parse(article)
                    break
                except:
                    pass
            if data_w["price"] != price or data_w["price_card"] != oz_price:
                change_price(data_w["price_card"], data_w["price"], article, chat_id)
                await bot.send_message(chat_id = int(chat_id), text= f"Цена на товар по артикулу {article} изменилась!\nТекущая цена: {data_w['price']}₽\nТекущая цена по Ozon карте: {data_w['price_card']}₽")
            time.sleep(120)
asyncio.run(main())