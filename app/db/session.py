from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_config


@lru_cache()
def get_engine():
    settings = get_config()
    return create_engine(settings.DATABASE_URL, future=True)


@lru_cache()
def get_session_local():
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
