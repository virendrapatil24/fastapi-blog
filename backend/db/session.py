from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print("Database URL: ", SQL_ALCHEMY_DATABASE_URL)
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()
