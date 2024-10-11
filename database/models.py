from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base


class User(Base):
    __tablename__ = 'users'

    # Описание основных данных о пользователях

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)

    ticket: Mapped[list["Ticket"]] = relationship(back_populates='user')

class Ticket(Base):
    __tablename__ = 'tickets'

    # Описание основных полей для тикетов
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    ticket_type: Mapped[str] = mapped_column(String, nullable=False)
    ticket_text: Mapped[str] = mapped_column(String, nullable=False)

    # Связи с пользователем
    user: Mapped["User"] = relationship(back_populates="tickets")
'''
Потом допишу функционал в отдельном форке
'''
# class Theme(Base):
#     __tablename__ = 'themes'

#     # Описание основных данных о темках

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     context: Mapped[str] = mapped_column(String, nullable=False)

#     user: Mapped[list["User"]] = relationship(back_populates="applications")

