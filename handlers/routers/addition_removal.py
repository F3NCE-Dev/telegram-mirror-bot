from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.database import SessionLocal, BeyondMessage
from aiogram.filters import Command
from aiogram import Router

router = Router()

class States(StatesGroup):
    waiting_for_confimation = State()

@router.message(Command("remove_addition"))
async def Remove_addition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.chat.id)
    await message.answer("Are you sure? (y/n)")
    await state.set_state(States.waiting_for_confimation)

@router.message(Command("remove_addition"))
async def Process_addition_removal(message: Message, state: FSMContext):
    await state.update_data(confirmation_state=message.text)
    
    data = await state.get_data()

    if data["confirmation_state"] == "y":
        db = SessionLocal()

        addition = db.query(BeyondMessage)

        if addition:
            db.delete(addition)
            db.commit()
        
        db.close()

        await message.answer("data has removed successfully")
    else:
        await message.answer("then I won't delete your message")
        
    await state.clear()
