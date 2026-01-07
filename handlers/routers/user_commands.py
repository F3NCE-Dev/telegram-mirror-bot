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
                                '\n/create - create a channel branch'
                                '\n/remove - remove a channel branch'
                                '\n/rename - rename your channel branch (/rename "old name" "new name")'
                                '\n/branches - list your channel branches'
                                '\n/send - send a message to a specific channel (/send "recipient ID" "message")'
                                '\n/addition - add something at the end of the messages'
                                '\n/removeextramessage - remove the extra message'
                                '\n/viewextramessage - view your current extra message'
                                '\n/enable - activate your channel branch (/enable "name")'
                                '\n/disable - deactivate your channel branch (/disable "name")', parse_mode='html')

@router.message(Command ('id'))
async def getID(message: Message):
    await message.answer(f'{message.chat.id}')

