from aiogram.dispatcher.filters.state import StatesGroup, State

class admin(StatesGroup):
    add = State()
    delete  =State()