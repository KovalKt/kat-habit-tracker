from datetime import datetime

from pydantic import BaseModel


class HabitBase(BaseModel):
    user_id: int
    name: str
    description: str | None = None
    frequency: str
    target_per_period: int


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    frequency: str | None = None
    target_per_period: int | None = None
    is_archived: bool | None = None


class HabitRead(HabitBase):
    id: int
    created_at: datetime
    is_archived: bool

    class Config:
        from_attributes = True
