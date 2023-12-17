from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .config import TELEGRAM_TOKEN

from .handlers import test_echo
from .middleware.db import DbSessionMiddleware
from .db.base import db_pool


async def bot_pooling() -> None:
    bot_ = Bot(token=TELEGRAM_TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(test_echo.router)

    dp.message.middleware(DbSessionMiddleware(db_pool))
    dp.callback_query.middleware(DbSessionMiddleware(db_pool))

    await dp.start_polling(bot_)