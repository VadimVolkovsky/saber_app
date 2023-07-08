from pydantic.dataclasses import dataclass


@dataclass
class BuildBase:
    """Базовый дата класс для билдов"""
    name: str


@dataclass
class Build(BuildBase):
    """Дата класс для отображения списка задач билда"""
    tasks: list
