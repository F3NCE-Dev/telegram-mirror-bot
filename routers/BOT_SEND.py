from aiogram.types import Message
from aiogram import Router
from bot import bot
from dependencies import Get_Branch_DB, Get_Addition_DB, Is_There_Addtion

router = Router()

@router.message()
async def send_message_byID(message: Message):
    user_id = message.chat.id
    for branch_name, input_id, output_id, status in Get_Branch_DB(user_id):
        if (message.chat.id == output_id) and status:
            if message.content_type == "text":
                Bot_message = message.text

                if Is_There_Addtion(user_id):
                    test = Get_Addition_DB(user_id)
                    Bot_message += f"\n\n{test}"

                await bot.send_message(chat_id=input_id, text=Bot_message)
            else:
                await message.copy_to(chat_id=input_id)
