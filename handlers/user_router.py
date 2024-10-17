from create_bot import bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from database.dao.dao import UserDAO, TicketDAO
from handlers.forms import SupportForm

from keyboards.inline_keyboadrs import start_inline_kb, themes_inline_kb, tikcket_inline_kb, types_tikcket_inline_kb, accept_or_cancle_kb
user_router = Router()

# Приветсвенный сообщение
@user_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    
    if not user:
        await UserDAO.add(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )


    caption = f"Добро пожаловать в 💸<b>StariyDed</b>💸\n" \
              f"Наша комманда поможет тебе обрести постоянный доход\n" \
              f" в сфере абуза аккаунтов различных банков\n\n" \
              f'<b>Присойденяйся:</b> @ded_afafafa'
    photo_url = 'https://i.postimg.cc/xTRGR02Q/start-photo.jpg'
    await message.answer_photo(caption=caption, reply_markup=start_inline_kb(message.from_user.id), photo=photo_url)

# Выдаёт все темы для пользователя
@user_router.callback_query(F.data == 'themes')
async def get_themes_list(call: CallbackQuery):
    await call.answer()
 
    text = 'У нас лучшее абузы по Aльфa бaнкy\n' \
           'Вот актуальные темки от деды:'
    
    await call.message.edit_caption(caption=text, reply_markup=themes_inline_kb())


# функция для выхода в меню
@user_router.callback_query(F.data == 'backtomenu')
async def go_to_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer()

    text =  f"Добро пожаловать в 💸<b>StariyDed</b>💸\n" \
            f"Наша комманда поможет тебе обрести постоянный доход\n" \
            f" в сфере абуза аккаунтов различных банков\n\n" \
            f'<b>Присойденяйся:</b> @ded_afafafa'

    await call.message.edit_caption(caption=text, reply_markup=start_inline_kb(call.from_user.id))

# Функция для вызова панели помощи
@user_router.callback_query(F.data == 'support')
async def get_support(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.clear()
    
    # text = 'Напиши мне о своей проблеме и наши админы свяжуться в течение дня'
    # await call.message.answer(text=text)

    text = 'Если нужна помощь, то нажми кнопку <i>"Создать тикет"</i>\n' \
           'и наши админы ответя тебе в течении 24-х часов'

    await call.message.edit_caption(caption=text, reply_markup=tikcket_inline_kb())

# Функция по выбору типа проблемы
@user_router.callback_query(F.data == 'ticket')
async def get_type_ticket(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.clear()
    
    text = 'Для начала выбери тип проблемы'
    await state.set_state(SupportForm.ticket_type)
    await call.message.edit_caption(text=text, reply_markup=types_tikcket_inline_kb())

# Функция по написания отзыва о проблеме
@user_router.callback_query(F.data.startswith('sup_'), SupportForm.ticket_type)
async def get_text_ticket(call: CallbackQuery, state: FSMContext):
    await call.answer()
    problem_type = call.data.split('sup_')[1]
    await state.update_data(ticket_type=problem_type)
    
    text = f'Тип вашей проблемы: {problem_type}\n\n'\
              f'Теперь опишите свою проблему:'
    
    await state.set_state(SupportForm.ticket_text)

    await call.message.answer(text=text)


# Функция по выбору сохранить или нет
@user_router.message(F.text, SupportForm.ticket_text)
async def accept_or_cancle_problem(message: Message, state: FSMContext):
    problem_text = message.text
    await state.update_data(ticket_text=problem_text)
       
    problem_data = await state.get_data()

    text = f'Тип вашей проблемы: {problem_data.get('ticket_type')}\n\n'\
            f'Текст вашей проблемы:\n{problem_data.get('ticket_text')}'
       
    await message.answer(text=text, reply_markup=accept_or_cancle_kb())

@user_router.callback_query(F.data == 'accept', SupportForm.ticket_text)
async def accept_problem(call: CallbackQuery, state: FSMContext):
    problem_data = await state.get_data()
    await call.answer('Ваше сообщение отправленно')
    await TicketDAO.add(
        user_id=call.from_user.id,
        username=call.from_user.username,
        ticket_type=problem_data.get('ticket_type'),
        ticket_text=problem_data.get('ticket_text')
    )
    await call.message.delete()


@user_router.callback_query(F.data == 'cancle')
async def cancle_problem(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('Ваше сообщение не было отправленно')

    await call.message.delete()