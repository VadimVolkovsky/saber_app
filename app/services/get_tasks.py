import logging
from app.models.build import Build


def get_sorted_tasks(build: Build, task_objects: list) -> list:
    """Получает отсортированный список задач для указанного билда"""
    sorted_tasks = []
    for task_name in build.tasks:
        for task in task_objects:
            if task_name == task.name:
                if task.dependencies:
                    sorted_tasks += task.dependencies
                sorted_tasks.append(task.name)
    logging.info(f'Получен список задач {sorted_tasks}')
    return sorted_tasks
