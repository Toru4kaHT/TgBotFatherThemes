from aiogram.fsm.state import State, StatesGroup

class SupportForm(StatesGroup):
    ticket_type = State()
    ticket_text = State()