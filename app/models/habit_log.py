from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from app.models.base import Base


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    completed_at = Column(DateTime, nullable=True)
    note = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
