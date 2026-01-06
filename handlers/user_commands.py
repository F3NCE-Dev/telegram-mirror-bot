from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.database import SessionLocal, Branch

router = Router()

@router.message(Command ("Start"))
async def StartMessage(message: Message):
    await message.answer("Hi! choose what you need")

@router.message(Command ('help'))
async def getHelp(message: Message):
    await message.answer('<b>My Commands:</b>'
                                '\n/id - show the current chat ID'
                                '\n/create - create a channel branch (/create "name" "output ID" "Input ID")'
                                '\n/remove - remove a channel branch (/remove "name")'
                                '\n/rename - rename your channel branch (/rename "old name" "new name")'
                                '\n/branches - list your channel branches'
                                '\n/send - send a message to a specific channel (/send "recipient ID" "message")'
                                '\n/extramessage - add something at the end of the messages (/extramessage "message")'
                                '\n/removeextramessage - remove the extra message'
                                '\n/viewextramessage - view your current extra message'
                                '\n/enable - activate your channel branch (/enable "name")'
                                '\n/disable - deactivate your channel branch (/disable "name")', parse_mode='html')

@router.message(Command ('id'))
async def getID(message: Message):
    await message.answer(f'{message.chat.id}')

@router.message(Command ('list'))
async def getList(message: Message):
    db = SessionLocal()

    rows = db.query(
        Branch.branch_name,
        Branch.input_id,
        Branch.output_id,
    ).all()

    db.close()

    if not rows:
        await message.answer("No branches found")
        return
    
    branch_list = "Your brances:"

    for branch_name, input_id, output_id in rows:
        branch_list += f"\n\n {branch_name}: {input_id} --------------> {output_id}"

    await message.answer(f'{branch_list}')
