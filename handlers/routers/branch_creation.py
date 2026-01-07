from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.database import SessionLocal, Branch
from aiogram.filters import Command
from aiogram import Router

router = Router()

class States(StatesGroup):
    waiting_for_name = State()
    waiting_for_in = State()
    waiting_for_out = State()

#User States
@router.message(Command("create"))
async def add_branch(message: Message, state: FSMContext):
    await state.update_data(user_id=message.chat.id)
    await message.answer("Enter your branch name")
    await state.set_state(States.waiting_for_name)

@router.message(States.waiting_for_name)
async def process_user_id(message: Message, state: FSMContext):
    await state.update_data(branch_name=message.text)
    await message.answer('type your "input id"')
    await state.set_state(States.waiting_for_in)

@router.message(States.waiting_for_in)
async def process_name(message: Message, state: FSMContext):
        await state.update_data(input_id=message.text)
        await message.answer('type your "output id"')
        await state.set_state(States.waiting_for_out)

@router.message(States.waiting_for_out)
async def process_out(message: Message, state: FSMContext):
        await state.update_data(output_id=message.text)
        data = await state.get_data()

        db = SessionLocal()
        branch = Branch(
            user_id = data["user_id"],
            branch_name = data["branch_name"],
            input_id = data["input_id"],
            output_id = data["output_id"],
        )
        db.add(branch)
        db.commit()
        
        db.close()

        await message.answer("data has received successfully")

        await state.clear()

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