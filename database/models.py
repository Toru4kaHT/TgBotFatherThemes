from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base


class User(Base):
    __tablename__ = 'users'

    # Описание основных данных о пользователях

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)

#     themes: Mapped[list["Theme"]] = relationship(back_populates='user')


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

