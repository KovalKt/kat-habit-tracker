from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.repositories.habit import HabitRepository
from app.repositories.habit_log import HabitLogRepository


class StatsService:
    def __init__(self, db: Session) -> None:
        self.habits = HabitRepository(db)
        self.logs = HabitLogRepository(db)

    def summary_for_user(self, user_id: int) -> dict[str, int]:
        habits = self.habits.list_active_by_user(user_id)
        return {
            "active_habits": len(habits),
            "archived_habits": max(len(self.habits.list_by_user(user_id)) - len(habits), 0),
        }

    def completions_last_7_days(self, habit_id: int) -> int:
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=7)
        return len(self.logs.list_completed_between(habit_id, start_date, end_date))
