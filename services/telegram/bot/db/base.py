from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from ..config import DATABASE_URI

engine = create_async_engine(DATABASE_URI, future=True, echo=False)

Base = declarative_base()

db_pool = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)