import asyncio

from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.routers import addition_creation, cancel_command, user_commands, branch_creation, branch_removal, addition_removal, branch_edit, list_db_commands, BOT_SEND

load_dotenv()
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token=getenv("BOT_TOKEN"))

async def main() -> None:
    dp.include_router(cancel_command.router)
    dp.include_router(branch_creation.router)
    dp.include_router(user_commands.router)
    dp.include_router(branch_removal.router)
    dp.include_router(addition_creation.router)
    dp.include_router(addition_removal.router)
    dp.include_router(branch_edit.router)
    dp.include_router(list_db_commands.router)
    dp.include_router(BOT_SEND.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
