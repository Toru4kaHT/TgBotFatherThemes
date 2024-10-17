from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import admins

# стартовая клава
def start_inline_kb(telegram_id: int):
    kb_list = [
        [InlineKeyboardButton(text='✈️ Наш тгк', url='https://t.me/nefor_py'),
         InlineKeyboardButton(text='📗 Помощь', callback_data='support')],
        [InlineKeyboardButton(text='💣 Темки', callback_data='themes')]
               ]
    if telegram_id in admins:
        kb_list[1].append(InlineKeyboardButton(text='👤 Админка', callback_data='admin'))
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    return keyboard

# клава выодится когда нужно вывести список темок
def themes_inline_kb():
    themes_list = {'1. Альфа банк': 'alfa',
                   '2. Рефки': 'refki',
                   '3. Пойти на работу': 'gotowork',
                   '4. Скам бабушек': 'scum',
                   '5. абуз карт': 'abuz',
                   '6. Нагорные челны': 'meow',
                   '7. Альфа банк': 'alfa',
                   '8. Рефки': 'refki',
                   '9. Пойти на работу': 'gotowork',
                   '10. Скам бабушек': 'scum',
                   }
    themes_button_list = [[InlineKeyboardButton(text=theme, callback_data=callback)] for theme, callback in themes_list.items()]
    kb_list = [
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='backtomenu'), 
         InlineKeyboardButton(text='📗 Помощь', callback_data='support')]
               ]
    kb_list = themes_button_list + kb_list
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    
    return keyboard

# клава для создания тикетов
def tikcket_inline_kb():
    kb_list = [
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='backtomenu'),
         InlineKeyboardButton(text='🎫 Создать тикет', callback_data='ticket')]
               ]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    return keyboard

def types_tikcket_inline_kb():
    kb_list = [
        [InlineKeyboardButton(text='🤖 Бот', callback_data='sup_bot'), InlineKeyboardButton(text='💸 Темка', callback_data='sup_theme')],
        [InlineKeyboardButton(text='👤 Пользователь', callback_data='sup_user'), InlineKeyboardButton(text='💬 Отзыв', callback_data='sup_feedback')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='support')]
    ]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    return keyboard

def accept_or_cancle_kb():
    kb_list = [
        [InlineKeyboardButton(text='✅ Да', callback_data='accept'), InlineKeyboardButton(text='❌ Нет', callback_data='cancle')]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    return keyboard