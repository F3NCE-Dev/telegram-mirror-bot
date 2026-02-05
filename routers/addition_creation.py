from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database import SessionLocal, BeyondMessage
from aiogram.filters import Command
from aiogram import Router

router = Router()

class States(StatesGroup):
    waiting_for_extra_message = State()

@router.message(Command("addition"))
async def Create_ExtraMessage(message: Message, state: FSMContext):
    await state.update_data(user_id=message.chat.id)
    await message.answer("Enter your message addition")
    await state.set_state(States.waiting_for_extra_message)

@router.message(States.waiting_for_extra_message)
async def Waiting_for_extra_message(message: Message, state: FSMContext):
    await state.update_data(extra=message.text)
    data = await state.get_data()

    with SessionLocal() as db:
        bm = BeyondMessage(
            user_id = data["user_id"],
            addition = data["extra"],
        )
        db.merge(bm)
        db.commit()

    await message.answer("addition has successfully added")
    await state.clear()

