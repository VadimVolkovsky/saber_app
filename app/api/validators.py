from http import HTTPStatus
import logging

from fastapi import HTTPException

from app.api.exceptions import (ExtraFieldsException, FieldNotFountException,
                                TasksListIsEmptyException)
from app.core.config import TASKS
from app.models.build import Build


def check_build_is_exists(build_objects: list, build_name: str) -> Build:
    """Проверяет, что указанный build существует. """
    for build in build_objects:
        if build.name == build_name:
            return build
    message = f'Билда с именем {build_name} не существует'
    logging.error(message)
    raise HTTPException(HTTPStatus.BAD_REQUEST, message)


def _check_required_fields(
        obj: dict,
        obj_fields: list,
        file_path: str,
) -> None:
    """Проверяет наличие обязательных полей в файле. """
    fields = obj.keys()
    for field in obj_fields:
        if field not in fields:
            message = f'отсутсвует поле {field} в файле {file_path}'
            logging.error(message)
            raise FieldNotFountException(message)


def _check_max_fields(obj: dict, obj_fields: list, file_path: str) -> None:
    """Проверяет наличие лишних полей в файле. """
    fields = obj.keys()
    if len(fields) > len(obj_fields):
        message = (
            f'Найдены лишние поля в файле {file_path}: {fields - obj_fields}')
        logging.error(message)
        raise ExtraFieldsException(message)


def _check_tasks_is_not_empty(obj) -> None:
    """Проверяет, что в билде присутствует минимум одна задача. """
    if TASKS in obj:
        if not obj.get('tasks'):
            message = (
                'Проверьте, что у всех билдов указана как минимум одна задача')
            logging.error(message)
            raise TasksListIsEmptyException(message)


def check_yaml_file_fields(
    obj: dict,
    obj_fields: list,
    file_path: str,
) -> None:
    """Проверяет поля переданного yaml файла. """
    _check_required_fields(obj, obj_fields, file_path)
    _check_max_fields(obj, obj_fields, file_path)
    _check_tasks_is_not_empty(obj)
