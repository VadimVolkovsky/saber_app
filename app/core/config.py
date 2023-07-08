from pydantic import BaseSettings

APP_NAME = "Saber App"
APP_DESCRIPTION = "Получить список задач для билда"
NAME = "name"
TASKS = "tasks"
DEPENDENCIES = "dependencies"
BUILD_FIELDS = [NAME, TASKS]
TASK_FIELDS = [NAME, DEPENDENCIES]
BUILDS_YAML_PATH = "builds/builds.yaml"
TASK_YAML_PATH = "builds/tasks.yaml"


class Settings(BaseSettings):
    app_title: str = APP_NAME
    app_description: str = APP_DESCRIPTION


settings = Settings()
