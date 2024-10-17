from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def admin_panel():
    kb_list = [[KeyboardButton(text='👤 Админка')]]

    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,)