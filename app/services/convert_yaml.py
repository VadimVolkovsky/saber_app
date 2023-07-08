
import logging
import yaml
from adaptix import Retort

from app.api.validators import check_yaml_file_fields
from app.core.config import (BUILD_FIELDS, BUILDS_YAML_PATH, TASK_FIELDS,
                             TASK_YAML_PATH)
from app.models.build import Build
from app.models.task import Task
from app.logging_config import configure_logging

retort = Retort()


def convert_builds_yaml_to_python_obj() -> list:
    """ Конвертирует builds.yaml в объект python"""
    build_objects = []
    try:
        with open(BUILDS_YAML_PATH) as f:
            data: dict = yaml.safe_load(f)
            for builds_list in data.values():
                for build in builds_list:
                    check_yaml_file_fields(
                        build, BUILD_FIELDS, BUILDS_YAML_PATH)
                    build = retort.load(build, Build)
                    build_objects.append(build)
    except FileNotFoundError:
        message = f'Проверьте наличие файла {BUILDS_YAML_PATH}'
        logging.error(message)
        raise FileNotFoundError(message)
    return build_objects


def convert_tasks_yaml_to_python_obj() -> list:
    """ Конвертирует tasks.yaml в объект python"""
    task_objects = []
    try:
        with open(TASK_YAML_PATH) as f:
            data = yaml.safe_load(f)
            for tasks_list in data.values():
                for task in tasks_list:
                    check_yaml_file_fields(task, TASK_FIELDS, TASK_YAML_PATH)
                    task = retort.load(task, Task)
                    task_objects.append(task)
    except FileNotFoundError:
        message = f'Проверьте наличие файла {TASK_YAML_PATH}'
        logging.error(message)
        raise FileNotFoundError(message)
    return task_objects


configure_logging()
task_objects = convert_tasks_yaml_to_python_obj()
build_objects = convert_builds_yaml_to_python_obj()
