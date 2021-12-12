import json

from fastapi import APIRouter

from app.crud.employee import EmployeeCRUD
from app.model.employee import Employee

router = APIRouter()


# TODO: Роутер для загрузки проверочных данных
@router.get("/load_testdata_database/", tags=["Data"])
async def load_data():
    """ Загрузка содержимого файла employees.json в базу данных mongo
    """
    with open('employees.json') as file:
        try:
            for employee in json.load(file):
                await EmployeeCRUD.create_employee(Employee(**employee))
            return 'Данные успешно сохранены!'
        except Exception as err:
            return f'Что то пошло не так:' \
                   f' {err}'
