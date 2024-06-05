from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup\

def otmena():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Отменить добавление артикула", callback_data="otm"))
    return kb