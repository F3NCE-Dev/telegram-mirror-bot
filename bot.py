import asyncio

from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.routers import addition_creation, user_commands, branch_creation, branch_removal, addition_removal

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token=BOT_TOKEN)

async def main() -> None:
    dp.include_router(branch_creation.router)
    dp.include_router(user_commands.router)
    dp.include_router(branch_removal.router)
    dp.include_router(addition_creation.router)
    dp.include_router(addition_removal.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
