from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command ("start"))
async def StartMessage(message: Message):
    await message.answer("Hi!\nUse help /help for detailed information")

@router.message(Command ('help'))
async def getHelp(message: Message):
    await message.answer('<b>My Commands:</b>'
                                '\n/id - show the current chat ID'
                                '\n/create - create a channel branch'
                                '\n/remove - remove a channel branch'
                                '\n/rename - rename your channel branch'
                                '\n/list - list your channel branches'
                                '\n/addition - add something at the end of the messages'
                                '\n/remove_addition - remove the addition'
                                '\n/viewad - view your current addition'
                                '\n/switch - change your branch status', parse_mode='html')

@router.message(Command ('id'))
async def getID(message: Message):
    await message.answer(f'{message.chat.id}')

