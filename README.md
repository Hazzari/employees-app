# API employee

#### Проект написан в рамках тестового задания:

```text
    Реализовать веб-приложение которое предоставляет собой один API метод для
    получения списка определенных сотрудников.
    Приложение должно быть асинхронным
    и реализовано с использованием FastAPI и MongoDB.
    
    Код должен выглядеть так, как отданный на ревью перед выпуском в продакшн.
    Если прод-реализация каких-то частей предполагает собой слишком
    сложный/большой кусок кода, то можно делать более простую реализацию
    и добавлять комментарий
    # TODO, в котором указать, какой вы видите окончательную реализацию данной фичи.
    
    Список данных прикреплен в json файле.
    Плюсом будет использование Docker, покрытие тестами.
```

Стек технологий:

```text
- python 3.10
- fastapi
- uvicorn
- odmantic (ODM)
- pytest
- pytest-dependency
```

Запуск проекта:
```text
.env - изменить под свои нужды и добавить в .gitignore
!!! При запуске на локальной машине не забыть поменять на MONGO_HOST=localhost
```

Запуск в докере:
```shell
docker-compose up --build -d 
```

Докер запускается по адресу: 
