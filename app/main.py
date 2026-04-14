from fastapi import FastAPI

from app.api.router import api_router
from app.core.exceptions import AppException, app_exception_handler


app = FastAPI(title="Kat Habit Tracker")
app.add_exception_handler(AppException, app_exception_handler)
app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to Kat Habit Tracker"}
