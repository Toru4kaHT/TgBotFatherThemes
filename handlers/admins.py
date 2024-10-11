from create_bot import bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboadrs import start_inline_kb, themes_inline_kb, tikcket_inline_kb
admin_router = Router()

