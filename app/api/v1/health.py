from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.common import HealthResponse


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)) -> HealthResponse:
    db_result = db.execute("SELECT 1").scalar()  # type: ignore
    if db != 1:
        raise HTTPException(
            status_code=503,
            detail="Health check failed",
        )
    
    return HealthResponse(status="ok")
