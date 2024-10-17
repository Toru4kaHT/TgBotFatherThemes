from create_bot import bot
from create_bot import admins
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboadrs import start_inline_kb, themes_inline_kb, tikcket_inline_kb
admin_router = Router()


@admin_router.callback_query(F.data == 'admin')
async def admin_panel(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.clear()

    text =  f"Привет {call.from_user.id}" \
            f"Наша комманда поможет тебе обрести постоянный доход\n" \
            f" в сфере абуза аккаунтов различных банков\n\n" \
            f'<b>Присойденяйся:</b> @ded_afafafa'

    await call.message.edit_caption(caption=text, reply_markup=start_inline_kb(call.from_user.id))