from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.habit_log import HabitLogCreate, HabitLogRead
from app.services.habit_service import HabitService


router = APIRouter()


@router.get("/", response_model=List[HabitLogRead])
def list_logs(habit_id: int, db: Session = Depends(get_db)) -> list[HabitLogRead]:
    service = HabitService(db)
    logs = service.list_logs(habit_id=habit_id)
    return [HabitLogRead.from_orm(log) for log in logs]


@router.post("/", response_model=HabitLogRead, status_code=status.HTTP_201_CREATED)
def create_log(payload: HabitLogCreate, db: Session = Depends(get_db)) -> HabitLogRead:
    service = HabitService(db)
    log = service.create_log(payload)
    return HabitLogRead.from_orm(log)
