# saber_app


### Описание:
Для разработки игр требуется билд-система, которая автоматизирует и ускоряет рутинные процессы.
Система оперирует понятиями “задача” и “билд”. 

Задача – это то, что нужно сделать.
Например: 
•	собрать ресурсы игры; 
•	скомпилировать .exe; 
•	запаковать игру;
и так далее.

Задача описывается уникальным именем (`name`) и ее зависимостями (`dependencies`) от других задач. Задача не может быть выполнена раньше, чем ее зависимости. 
Описания задач задаются в yaml-файле `tasks.yaml` (в приложении).

Билд – это группа задач, объединенных функционально. 
Например:
•	"собрать игру" с задачами "собрать ресурсы игры", "скомпилировать .exe", "запаковать игру";
•	"запустить тесты" с задачами "собрать ресурсы игры", "скомпилировать .exe";
и так далее.

Билд описывается уникальным именем (`name`) и списком задач (`tasks`).
Описания билдов задаются в yaml-файле `builds.yaml` (в приложении).


### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git@github.com:VadimVolkovsky/saber_app.git
```

**Из корневой директории проекта выполните запуск контейнеров:**
```
docker-compose up --build
```

Будет выполнено разворачивание контейнера `backend`


### Логирование:
В приложении реализовано логирование.

Логи приложения (сервера) сохраняются здесь:
```
app/logs/
```


### Документация приложения:
- Swagger
```
http://127.0.0.1/docs
```

- Redoc
```
http://127.0.0.1/redoc
```


### Дополнительные возможности:
Тестирование через интерфейс Swagger:

Перейдите в браузере по адресу:
```
http://127.0.0.1/docs
```

В интерактивном меню Swagger, во вкладке POST /get_tasks/ нажмите кнопку "Try it out"

Заполните Request body:
```
{
    "name": "forward_interest"
}
```

Нажмите кнопку "Execute"(выполнить)

В ответе будет отображены задачи для указанного билда, отсортированные с учетом зависимостей:

```
[
  "build_teal_leprechauns",
  "bring_olive_centaurs",
  "create_maroon_centaurs",
  "create_olive_centaurs",
  "coloring_aqua_centaurs",
  "coloring_aqua_golems",
  "coloring_navy_golems",
  "map_olive_leprechauns",
  "enable_lime_leprechauns",
  "map_olive_leprechauns",
  "enable_lime_leprechauns",
  "create_aqua_humans",
  "enable_olive_humans",
  "create_purple_humans",
  "train_white_humans",
  "write_teal_humans",
  "enable_silver_humans",
  "enable_fuchsia_ogres",
  "upgrade_navy_ogres",
  "write_blue_ogres",
  "write_fuchsia_golems"
]
```


### Технологии:
- Python 3.10
- FastAPI
