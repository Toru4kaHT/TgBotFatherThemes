from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from database.dao.base import BaseDAO
from database.models import User, Ticket
from database.database import async_session_maker

class UserDAO(BaseDAO):
    model = User

class TicketDAO(BaseDAO):
    model = Ticket
