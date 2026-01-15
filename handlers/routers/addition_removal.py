from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.database import SessionLocal, BeyondMessage
from aiogram.filters import Command
from aiogram import Router
from handlers.DB_HANDLER import Is_There_Addtion

router = Router()

class States(StatesGroup):
    waiting_for_confimation = State()

@router.message(Command("remove_addition"))
async def Remove_addition(message: Message, state: FSMContext):
    if Is_There_Addtion(message.chat.id):
        await state.update_data(user_id=message.chat.id)
        await message.answer("Are you sure? (y/n)")
        await state.set_state(States.waiting_for_confimation)
    else:
        await message.answer("You have no addition")

@router.message(States.waiting_for_confimation)
async def Process_addition_removal(message: Message, state: FSMContext):
    await state.update_data(confirmation_state=message.text)
    
    data = await state.get_data()

    if data["confirmation_state"] == "Y" or "y":
        db = SessionLocal()

        addition = db.query(BeyondMessage).filter(BeyondMessage.user_id == data["user_id"]).first()

        db.delete(addition)
        db.commit()
        
        db.close()

        await message.answer("data has removed successfully")
    else:
        await message.answer("then I won't delete your message")
        
    await state.clear()
