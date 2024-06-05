from aiogram import Dispatcher
from tg_bot.parsers import ozon_parse
from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from tg_bot.states import admin
from tg_bot.DBSM import add, check
from tg_bot.keyboards import otmena
import requests
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(add_article_proc, state = admin.add)
    dp.register_callback_query_handler(refuse, state = admin.add)
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(add_article, commands=["add"])


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Здравствуйте! Чтобы добавить в список отслеживаемых артикулов новый артикул, введите /add, а я получу информацию о товаре и начну отслеживать изменение цены.")


async def add_article(message: types.Message, state: FSMContext):
    await message.answer("Введите артикул в следующем сообщении", reply_markup= otmena())
    await admin.add.set()


async def add_article_proc(message: types.Message, state: FSMContext):
    if not check(message.text, message.chat.id):
        await message.answer("Вы уже получаете уведомления о изменениях цены этого товара")
        await state.finish()
        return
    mess = await message.answer("Собираю информацию о товаре...")
    result = ozon_parse(message.text)
    await mess.delete()
    if result == False:
        await message.answer("Упс, такого артикула не существует... Введите, пожалуйста, заново или отмените добавление", reply_markup= otmena())
        return
    else:
        add(message.text, result["photo"], message.chat.id, int(result['price']), int(result['price_card']))
        text = f"<b>Название товара:</b> {result['name']}\n<b>Цена по Ozon карте:</b> {result['price_card']}₽\n<b>Цена без Ozon карты:</b>{result['price']}₽\n\n<b><i>Отслеживание цены товара включено(Вы будете получать уведомления, когда цена изменится)</i></b>"
        url = result["photo"]
        img_data = requests.get(url).content
        with open('image.jpg', 'wb') as handler:
            handler.write(img_data)
        with open('image.jpg', 'rb') as handler:
            await message.answer_photo(photo=handler, caption=text)
        
    await state.finish()
        

async def refuse(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("Готово. Если заходите добавить артикул, введите /add")

    

    