from aiogram.types import Message
from aiogram import Router
from bot import bot
from handlers.GETDB import *

router = Router()

@router.message_handler()
async def send_message_byID(message: Message):
    for input_id, output_id in Get_Branch_DB:
        if (message.chat.id == output_id):
            
            messageID = message.chat.id

            if Get_Addition_DB(messageID):
                test = Get_Addition_DB(messageID)

            await bot.send_message(chat_id=input_id, text=message)

