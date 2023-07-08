
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.validators import check_build_is_exists
from app.services.convert_yaml import build_objects, task_objects
from app.services.get_tasks import get_sorted_tasks

router = APIRouter()


@router.post(
    "/get_tasks/",
    response_class=JSONResponse,
    description="Эндпоинт для получения списка заданий (tasks). ",
)
async def get_tasks(
    build_name: str,
):
    build = check_build_is_exists(build_objects, build_name)
    return get_sorted_tasks(build, task_objects)
