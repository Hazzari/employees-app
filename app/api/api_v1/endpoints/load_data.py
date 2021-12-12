import json

from fastapi import APIRouter

from app.crud.user import UserCRUD
from app.model.user import User

router = APIRouter()


# TODO: Роутер для загрузки проверочных данных
@router.get("/load_testdata_database/", tags=["Load test date to database"])
async def load_data():
    """ Загрузка содержимого файла employees.json в базу данных mongo
    """
    with open('employees.json') as file:
        try:
            for user in json.load(file):
                await UserCRUD.create_user(User(**user))
            return 'Данные успешно сохранены!'
        except Exception as e:
            return f'Что то пошло не так:' \
                   f' {e}'
