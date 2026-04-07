from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey
from .base import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    frequency = Column(String, nullable=False)  # daily / weekly
    target_per_period = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    is_archived = Column(Boolean, nullable=False, default=False)
