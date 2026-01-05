import asyncio

from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.appointment import router
from aiogram.filters import Command
from aiogram.types import Message

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(Command ("Start"))
async def StartMessage(message: Message):
    await message.answer("Hi!")

async def main() -> None:
    try:
        bot = Bot(token=BOT_TOKEN)
        dp.include_router(router=router)
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"an error: {ex}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
