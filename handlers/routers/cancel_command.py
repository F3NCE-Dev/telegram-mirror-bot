from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("cancel"))
async def cancel_fsm_text(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("then i won't do that")
