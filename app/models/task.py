from pydantic.dataclasses import dataclass


@dataclass
class Task:
    """Дата класс для заданий"""
    name: str
    dependencies: list
