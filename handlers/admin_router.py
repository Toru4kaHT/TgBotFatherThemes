from create_bot import bot
from create_bot import admins
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from keyboards.inline_keyboadrs import admin_panel_kb, pick_tickets_type_kb
admin_router = Router()

# Главная админ панель
@admin_router.callback_query(F.data == 'admin')
async def admin_panel(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.clear()

    text =  f"Привет {call.from_user.first_name}\n" \
            f"Ты попал в админ панель 🤫"\

    await call.message.edit_caption(caption=text, reply_markup=admin_panel_kb())

@admin_router.callback_query(F.data == 'adm_tickets')
async def pick_tickets_type(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.clear()

    text = f'Выбери тип проблемы по твоему\nроду деятельности:'

    await call.message.edit_caption(caption=text, reply_markup=pick_tickets_type_kb())

# @admin_router.callback_query(F.data.startswith('type_'))
# async def generic_types(call: CallbackQuery, state: FSMContext):
#         tickets = call.data.split('type_')[1]
#         await call.message.edit_caption(caption='Пользователи у которых проблемы:', reply_markup=generic_tickets_kb(tickets))
