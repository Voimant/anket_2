from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


admin_button = [
    [InlineKeyboardButton(text='Заменить администратора на 3 тега', callback_data='change_3')],
    [InlineKeyboardButton(text='Заменить администратора на 4 тега', callback_data='change_4')],
    [InlineKeyboardButton(text='Скачать базу', callback_data='upload_base')]
]

admin_markup = InlineKeyboardMarkup(inline_keyboard=admin_button)