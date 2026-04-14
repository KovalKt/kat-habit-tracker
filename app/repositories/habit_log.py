from datetime import datetime

from app.models.habit_log import HabitLog
from app.repositories.base import BaseRepository


class HabitLogRepository(BaseRepository[HabitLog]):
    model = HabitLog

    def list_by_habit(self, habit_id: int) -> list[HabitLog]:
        return self.db.query(HabitLog).filter(HabitLog.habit_id == habit_id).all()

    def list_completed_between(
        self,
        habit_id: int,
        start_date: datetime,
        end_date: datetime,
    ) -> list[HabitLog]:
        return (
            self.db.query(HabitLog)
            .filter(
                HabitLog.habit_id == habit_id,
                HabitLog.completed_at >= start_date,
                HabitLog.completed_at <= end_date,
            )
            .all()
        )
