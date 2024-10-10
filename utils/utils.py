from create_bot import admins
from aiogram.types import Message


class Admin():
    def __init__(self) -> None:
        self.admins = admins
    
    def is_admin(message: Message):
        if message.from_user.id in admins:
            return True
        else:
            return False
    
    def delite_admin():
        pass