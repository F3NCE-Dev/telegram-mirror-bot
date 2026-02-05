from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from dependencies import Get_Addition_DB, Get_Branch_DB, Is_There_Branch, Is_There_Addtion

router = Router()

@router.message(Command ('list'))
async def getList(message: Message):
    user_id = message.chat.id
    
    if not Is_There_Branch(user_id):
        await message.answer("No branches found")
        return
    
    branch_list = "Your brances:"

    for branch_name, input_id, output_id, status in Get_Branch_DB(user_id):
        status_smile = "✅"

        if not status:
            status_smile = "❌"

        branch_list += f"\n\n {branch_name}: {output_id} --------------> {input_id} {status_smile}"

    await message.answer(f'{branch_list}')

@router.message(Command ('viewad'))
async def getAddtion(message: Message):
    chat_id = message.chat.id
    if Is_There_Addtion(chat_id):
        await message.answer(f'Your addition is "{Get_Addition_DB(chat_id)}"')
    else:
        await message.answer("You have no an addition")
