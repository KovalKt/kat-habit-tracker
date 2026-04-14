from datetime import date

from app.models.habit_log import HabitLog


class StreakService:
    def calculate_streak(self, logs: list[HabitLog]) -> int:
        completed_days = sorted(
            {
                log.completed_at.date()
                for log in logs
                if log.completed_at is not None
            },
            reverse=True,
        )
        if not completed_days:
            return 0

        streak = 0
        expected_day = completed_days[0]

        for completed_day in completed_days:
            if completed_day == expected_day:
                streak += 1
                expected_day = expected_day.fromordinal(expected_day.toordinal() - 1)
            else:
                break

        return streak

    def current_streak_from_dates(self, dates: list[date]) -> int:
        normalized_logs = [type("Log", (), {"completed_at": value}) for value in dates]
        return self.calculate_streak(normalized_logs)
