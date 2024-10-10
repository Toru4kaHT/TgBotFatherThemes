from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# стартовая клава
def start_inline_kb():
    kb_list = [
        [InlineKeyboardButton(text='💣 Темки', callback_data='themes'), 
         InlineKeyboardButton(text='📗 Помощь', callback_data='support')],
        [InlineKeyboardButton(text='✈️ Наш тгк', url='https://t.me/nefor_py')]
               ]
    
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