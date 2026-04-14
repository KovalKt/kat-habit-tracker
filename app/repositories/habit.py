from app.models.habit import Habit
from app.repositories.base import BaseRepository


class HabitRepository(BaseRepository[Habit]):
    model = Habit

    def list_by_user(self, user_id: int) -> list[Habit]:
        return self.db.query(Habit).filter(Habit.user_id == user_id).all()

    def list_active_by_user(self, user_id: int) -> list[Habit]:
        return (
            self.db.query(Habit)
            .filter(Habit.user_id == user_id, Habit.is_archived.is_(False))
            .all()
        )
