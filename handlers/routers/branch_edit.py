from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.DB_HANDLER import Set_Branch_Name, Is_There_Branch, Is_There_Branch_With_Name, Set_Branch_Status, Get_Branch_Status
from aiogram.filters import Command
from aiogram import Router

router = Router()

class RenameStates(StatesGroup):
    waiting_for_old_branch_name = State()
    waiting_for_new_branch_name = State()

@router.message(Command("rename"))
async def Rename_Branch(message: Message, state: FSMContext):
    user_id = message.chat.id
    if Is_There_Branch(user_id):
        await state.update_data(user_id=user_id)
        await message.answer("Enter your old branch name")
        await state.set_state(RenameStates.waiting_for_old_branch_name)
    else:
        await message.answer("You have no branches")

@router.message(RenameStates.waiting_for_old_branch_name)
async def Waiting_for_old_name(message: Message, state: FSMContext):
    if Is_There_Branch_With_Name(message.chat.id, message.text):
        await state.update_data(oldname=message.text)
        await message.answer("Enter your new branch name")
        await state.set_state(RenameStates.waiting_for_new_branch_name)
    else:
        await message.answer("There is no branch with that name")

@router.message(RenameStates.waiting_for_new_branch_name)
async def Waiting_for_new_name(message: Message, state: FSMContext):
    await state.update_data(newname=message.text)

    data = await state.get_data()

    Set_Branch_Name(data["user_id"], data["oldname"], data["newname"])
    await message.answer("Successfully!")

    await state.clear()

class SwitchStates(StatesGroup):
    waiting_for_branch_name = State()

@router.message(Command("switch"))
async def Switch_Branch(message: Message, state: FSMContext):
    if Is_There_Branch(message.chat.id):
        await message.answer("Enter the name of the branch you want to change")
        await state.set_state(SwitchStates.waiting_for_branch_name)
    else:
        await message.answer("You have no branches")

@router.message(SwitchStates.waiting_for_branch_name)
async def Process_Switch(message: Message, state: FSMContext):
    branch_name = message.text
    user_id = message.chat.id

    if Is_There_Branch_With_Name(user_id, branch_name):
        Set_Branch_Status(user_id, branch_name, not Get_Branch_Status)
        await message.answer("Successfully!")
    else:
        await message.answer("There is no branch with that name")

    await state.clear()
