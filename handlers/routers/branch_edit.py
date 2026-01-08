from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.DB_HANDLER import Set_Branch_Name, BranchNotFoundError
from aiogram.filters import Command
from aiogram import Router

router = Router()

class States(StatesGroup):
    waiting_for_old_branch_name = State()
    waiting_for_new_branch_name = State()

@router.message(Command("rename"))
async def Rename_Branch(message: Message, state: FSMContext):
    await state.update_data(user_id=message.chat.id)
    await message.answer("Enter your old branch name")
    await state.set_state(States.waiting_for_old_branch_name)

@router.message(States.waiting_for_old_branch_name)
async def Waiting_for_old_name(message: Message, state: FSMContext):
    await state.update_data(oldname=message.text)
    await message.answer("Enter your new branch name")
    await state.set_state(States.waiting_for_new_branch_name)

@router.message(States.waiting_for_new_branch_name)
async def Waiting_for_new_name(message: Message, state: FSMContext):
    await state.update_data(newname=message.text)

    data = await state.get_data()

    try:
        Set_Branch_Name(data["user_id"], data["oldname"], data["newname"])
        await message.answer("Successfully!")
    except BranchNotFoundError:
        await message.answer("There is no branch with that name")
    except Exception as e:
        await message.answer(f"{e}")

    await state.clear()

class States(StatesGroup):
    waiting_for_branch_name = State()

@router.message(Command("switch"))
async def Rename_Branch(message: Message, state: FSMContext):
    await state.update_data(user_id=message.chat.id)
    await message.answer("Enter the name of the branch you want to change")
    await state.set_state(States.waiting_for_branch_name)
