from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.database import SessionLocal, Branch
from aiogram.filters import Command
from aiogram import Router

router = Router()

class States(StatesGroup):
    waiting_for_branch_name = State()
    waiting_for_confirmation = State()

@router.message(Command ("remove"))
async def add_branch(message: Message, state: FSMContext):
    await message.answer("Enter the of the branch you want to remove")
    await state.set_state(States.waiting_for_branch_name)

@router.message(States.waiting_for_branch_name)
async def get_branch_name(message: Message, state: FSMContext):
    await state.update_data(branch_name=message.text)
    await message.answer(f'Are you sure you want to delete "{message.text}"? (y/n)')
    await state.set_state(States.waiting_for_confirmation)

@router.message(States.waiting_for_confirmation)
async def wait_for_confirmation(message: Message, state: FSMContext):
    await state.update_data(confirmation_state=message.text)
    
    data = await state.get_data()

    if data["confirmation_state"] == "y":
        db = SessionLocal()

        branch = db.query(Branch).filter(Branch.branch_name == data["branch_name"]).first()

        if branch:
            db.delete(branch)
            db.commit()
        
        db.close()

        await message.answer("data has removed successfully")

    else:
        await message.answer("then i won't delete your branch")

    await state.clear()
