from aiogram import Router, F, enums
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile

from admin_keyboards import admin_markup
from keyboards import main_menu_markup, sender_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from keyboards import cancel_markup, profile_markup, location_markup, work_mode_markup, back_markup
from aiogram import Dispatcher, Bot
from config import TOKEN
from DB.db_main import add_candidats, export_csv
from DB.DB import conn

bot = Bot(token=TOKEN)
router = Router()


@router.message(F.text == 'sfgfgafg')
async def get_admin(mess: Message, state: FSMContext):
    await mess.answer('ПАНЕЛЬ АДМИНИСТРАТОРА', reply_markup=admin_markup)


class FsmTag(StatesGroup):
    chat_id = State()
    go_change = State()


@router.callback_query(F.data == 'change_3')
async def change_3(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите новый chat_id для 3 тегов', reply_markup=cancel_markup)
    await state.set_state(FsmTag.chat_id)


@router.message(FsmTag.chat_id)
async def get_chat_id3(mess: Message, state: FSMContext):
    try:
        int(mess.text)
        with open('tegs_3.txt', 'w') as f:
            f.write(mess.text)
            await state.clear()
            await mess.answer('chat_id для 3 тегов изменен', reply_markup=admin_markup)
    except ValueError:
        await mess.answer('Введите chat_id цифрами', reply_markup=admin_markup)
        await state.clear()


class FsmTags(StatesGroup):
    chat_id = State()
    go_change = State()


@router.callback_query(F.data == 'change_4')
async def change_4(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите новый chat_id для 4 тегов', reply_markup=cancel_markup)
    await state.set_state(FsmTags.chat_id)


@router.message(FsmTags.chat_id)
async def get_chat_id4(mess: Message, state: FSMContext):
    try:
        int(mess.text)
        with open('tegs_4.txt', 'w') as f:
            f.write(mess.text)
        await state.clear()
        await mess.answer('chat_id для 4 тегов изменен', reply_markup=admin_markup)
    except ValueError:
        await mess.answer('Введите chat_id цифрами', reply_markup=admin_markup)
        await state.clear()


@router.callback_query(F.data == 'upload_base')
async def upload_base(call: CallbackQuery):
    export_csv()
    file = FSInputFile('results.csv')
    await call.message.answer_document(file, caption='Документ отправлен', reply_markup=admin_markup)
