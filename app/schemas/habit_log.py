from datetime import datetime

from pydantic import BaseModel


class HabitLogBase(BaseModel):
    habit_id: int
    note: str | None = None


class HabitLogCreate(HabitLogBase):
    completed_at: datetime | None = None


class HabitLogRead(HabitLogBase):
    id: int
    completed_at: datetime | None = None
    created_at: datetime

    class Config:
        orm_mode = True
