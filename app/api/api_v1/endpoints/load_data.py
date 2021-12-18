import json

from fastapi import APIRouter, HTTPException
from fastapi import status

from app.core.config import MONGO_DB
from app.database.database import client

router = APIRouter()


# TODO: Роутер для загрузки проверочных данных
@router.get("/load_testdata_database/",
            tags=["Data"],
            status_code=status.HTTP_201_CREATED
            )
async def load_data():
    """ Загрузка содержимого файла employees.json в базу данных mongo
    """

    try:
        with open('employees.json') as file:
            employees = json.loads(file.read())
            db = client[MONGO_DB]
            await db[MONGO_DB].insert_many(employees)
            return 'Начальные данные успешно загружены'
    except FileNotFoundError:
        raise HTTPException(status_code=404,
                            detail="File employees.json not found")
    except TypeError:
        raise HTTPException(status_code=412,
                            detail="Данные в файле employees.json не валидны")
