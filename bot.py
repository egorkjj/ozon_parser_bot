import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_bot.handlers import register_handlers
from tg_bot.parsers import run_selenium
storage = MemoryStorage()
logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_handlers(dp)

async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    bot = Bot(token='7421677549:AAGHL5x8EWp3QhWQI1CdKVF1U2cOaDmxPRQ', parse_mode = 'HTML')
    dp = Dispatcher(bot, storage=storage) 
    register_all_handlers(dp)
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())