from environs import Env
from aiogram import Bot
from tg_bot.DBSM import fetchall, change_price
from tg_bot.parsers import ozon_parse
import asyncio
env = Env()
env.read_env(".env")
token = env.str("BOT_TOKEN")
print(token)

async def main():
    bot = Bot(token = token)
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
        

asyncio.run(main())