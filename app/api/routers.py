from fastapi import APIRouter

from app.api.endpoints import tasks_router

main_router = APIRouter()
main_router.include_router(
    tasks_router,
    tags=['Tasks'],
)
