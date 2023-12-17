import datetime

from sqlalchemy import Column, Integer, BigInteger, Enum

from .base import Base
from ..enums.roles import Roles


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)


class User(BaseModel):
    __tablename__ = 'users'

    telegram_id = Column(BigInteger, index=True, nullable=False)
    role = Column(Enum(Roles), nullable=False)
