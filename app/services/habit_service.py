from sqlalchemy.orm import Session

from app.core.exceptions import AppException
from app.repositories.habit import HabitRepository
from app.repositories.habit_log import HabitLogRepository
from app.schemas.habit import HabitCreate, HabitUpdate
from app.schemas.habit_log import HabitLogCreate


class HabitService:
    def __init__(self, db: Session) -> None:
        self.habits = HabitRepository(db)
        self.logs = HabitLogRepository(db)

    def list_habits(self, user_id: int):
        return self.habits.list_by_user(user_id)

    def create_habit(self, payload: HabitCreate):
        return self.habits.create(**payload.dict())

    def update_habit(self, habit_id: int, payload: HabitUpdate):
        habit = self.habits.get(habit_id)
        if habit is None:
            raise AppException("Habit not found", status_code=404)

        data = payload.dict(exclude_none=True)
        return self.habits.update(habit, **data)

    def list_logs(self, habit_id: int):
        return self.logs.list_by_habit(habit_id)

    def create_log(self, payload: HabitLogCreate):
        habit = self.habits.get(payload.habit_id)
        if habit is None:
            raise AppException("Habit not found", status_code=404)

        return self.logs.create(**payload.dict())
