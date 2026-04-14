from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.habit import HabitCreate, HabitRead, HabitUpdate
from app.services.habit_service import HabitService


router = APIRouter()


@router.get("/", response_model=List[HabitRead])
def list_habits(user_id: int, db: Session = Depends(get_db)) -> list[HabitRead]:
    service = HabitService(db)
    habits = service.list_habits(user_id=user_id)
    return [HabitRead.from_orm(habit) for habit in habits]


@router.post("/", response_model=HabitRead, status_code=status.HTTP_201_CREATED)
def create_habit(payload: HabitCreate, db: Session = Depends(get_db)) -> HabitRead:
    service = HabitService(db)
    habit = service.create_habit(payload)
    return HabitRead.from_orm(habit)


@router.patch("/{habit_id}", response_model=HabitRead)
def update_habit(
    habit_id: int,
    payload: HabitUpdate,
    db: Session = Depends(get_db),
) -> HabitRead:
    service = HabitService(db)
    habit = service.update_habit(habit_id, payload)
    return HabitRead.from_orm(habit)
