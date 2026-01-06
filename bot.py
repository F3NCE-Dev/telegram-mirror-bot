import asyncio

from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import user_commands, branch_creation, branch_removal

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def main() -> None:
    try:
        bot = Bot(token=BOT_TOKEN)
        dp.include_router(branch_creation.router)
        dp.include_router(user_commands.router)
        dp.include_router(branch_removal.router)
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"an error: {ex}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
