from aiogram.types import Message
from src.database import SessionLocal, Branch
from aiogram.filters import Command
from aiogram import Router

from handlers.DB_HANDLER import Get_Addition_DB, Get_Branch_DB

router = Router()

@router.message(Command ('list'))
async def getList(message: Message):
    user_id = message.chat.id
    if not Get_Branch_DB(user_id):
        await message.answer("No branches found")
        return
    
    branch_list = "Your brances:"

    for branch_name, input_id, output_id in Get_Branch_DB(user_id):
        branch_list += f"\n\n {branch_name}: {output_id} --------------> {input_id}"

    await message.answer(f'{branch_list}')

@router.message(Command ('viewad'))
async def getAddtion(message: Message):
    if Get_Addition_DB:
        await message.answer(f'Your addition is "{Get_Addition_DB}"')
    else:
        await message.answer("You have no an addition")
