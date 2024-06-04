from aiogram import Dispatcher
from tg_bot.parsers import ozon_parse
from aiogram import types
from aiogram.dispatcher import FSMContext
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])

async def cmd_start(message: types.Message, state: FSMContext):
    mess = await message.answer("Подождите немного, собираю информацию о товаре...")
    res = ozon_parse(1398829977)
    await mess.edit_text(res)

    

    