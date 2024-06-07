from aiogram import Bot
from tg_bot.DBSM import fetchall, change_price
from tg_bot.parsers import ozon_parse
import asyncio
import time

async def main():  
    print('flag1')
    bot = Bot(token = '7421677549:AAGHL5x8EWp3QhWQI1CdKVF1U2cOaDmxPRQ')
    while True:
        print('flag2')
        data = fetchall()
        for i in data:
            print('flag3')
            chat_id = i.user_id
            if i.card_price == None or i.card_price == 'None':
                oz_price = 0
            else:
                oz_price = int(i.card_price)
            
            price = int(i.price)
            article = i.article
            while True:
                try:
                    data_w = ozon_parse(article)
                    break
                except:
                    pass
            if data_w['price_card'] == None:
                continue
            if data_w["photo"] == "None":
                continue
            if data_w["price"] != price or data_w["price_card"] != oz_price:
                change_price(data_w["price_card"], data_w["price"], article, chat_id)
                if oz_price != 0:
                    await bot.send_message(chat_id = int(chat_id), text= f"Цена на товар по артикулу {article} изменилась!\nТекущая цена: {data_w['price']}₽\nТекущая цена по Ozon карте: {data_w['price_card']}₽")
            time.sleep(20)
        time.sleep(120)
asyncio.run(main())