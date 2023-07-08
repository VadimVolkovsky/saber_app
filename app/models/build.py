from dataclasses import dataclass


@dataclass
class Build:
    """Дата класс для билдов"""
    name: str
    tasks: list
