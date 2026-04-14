from datetime import datetime

from pydantic import BaseModel


class TimestampSchema(BaseModel):
    created_at: datetime

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str
