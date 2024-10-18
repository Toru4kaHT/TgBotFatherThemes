from create_bot import bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from database.dao.dao import UserDAO, TicketDAO
from handlers.forms import SupportForm


from keyboards.inline_keyboadrs import start_inline_kb, themes_inline_kb, tikcket_inline_kb, types_tikcket_inline_kb, accept_or_cancle_kb

ticket_router = Router()

# Функция по выбору типа проблемы
@ticket_router.callback_query(F.data == 'ticket')
async def get_type_ticket(call: CallbackQuery, state: FSMContext):
    await state.clear()
    ticket = TicketDAO.find_one_or_none(user_id=call.from_user.id)
    if ticket is not None:
        await call.answer()
        text = 'Для начала выбери тип проблемы'
        await state.set_state(SupportForm.ticket_type)
        await call.message.edit_caption(text=text, reply_markup=types_tikcket_inline_kb())
    else:
        await call.answer('Вы уже создали тикет. Подаждите пока наши\nадмины не ответят на него')
        
# Функция по написания отзыва о проблеме
@ticket_router.callback_query(F.data.startswith('sup_'), SupportForm.ticket_type)
async def get_text_ticket(call: CallbackQuery, state: FSMContext):
    await call.answer()
    problem_type = call.data.split('sup_')[1]
    await state.update_data(ticket_type=problem_type)
    
    text = f'Тип вашей проблемы: {problem_type}\n\n'\
              f'Теперь опишите свою проблему:'
    
    await state.set_state(SupportForm.ticket_text)

    await call.message.answer(text=text)


# Функция по выбору сохранить или нет
@ticket_router.message(F.text, SupportForm.ticket_text)
async def accept_or_cancle_problem(message: Message, state: FSMContext):
    problem_text = message.text
    await state.update_data(ticket_text=problem_text)
       
    problem_data = await state.get_data()

    text = f'Тип вашей проблемы: {problem_data.get('ticket_type')}\n\n'\
            f'Текст вашей проблемы:\n{problem_data.get('ticket_text')}'
       
    await message.answer(text=text, reply_markup=accept_or_cancle_kb())

@ticket_router.callback_query(F.data == 'accept', SupportForm.ticket_text)
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


@ticket_router.callback_query(F.data == 'cancle')
async def cancle_problem(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('Ваше сообщение не было отправленно')

    await call.message.delete()