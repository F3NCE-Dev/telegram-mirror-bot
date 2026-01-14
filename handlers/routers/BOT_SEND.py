from aiogram.types import Message
from aiogram import Router
from bot import bot
from handlers.DB_HANDLER import *

router = Router()

@router.message()
async def send_message_byID(message: Message):
    user_id = message.chat.id
    for branch_name, input_id, output_id in Get_Branch_DB(user_id):
        if (message.chat.id == output_id):
            if message.content_type == "text":
                Bot_message = message.text

                if Get_Addition_DB(user_id):
                    test = Get_Addition_DB(user_id)
                    Bot_message += f"\n\n{test}"

                await bot.send_message(chat_id=input_id, text=Bot_message)
            else:
                await message.copy_to(chat_id=input_id)
