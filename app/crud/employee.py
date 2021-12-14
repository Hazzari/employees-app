import re
from dataclasses import dataclass

from fastapi import APIRouter, HTTPException
from odmantic import ObjectId, query

from app.database.database import engine
from app.model.employee import Employee

router = APIRouter()


@dataclass
class EmployeeCRUD:
    model = Employee

    @classmethod
    async def get_employees(cls):
        """ Список всех сотрудников
        """
        document = await engine.find(cls.model)
        return document

    @classmethod
    async def count_employees(cls):
        """ Всего сотрудников в базе
        """
        count = await engine.count(cls.model)
        return count

    @classmethod
    async def get_employee_by_id(cls, id: ObjectId):
        """ Поиск сотрудника по id
        """

        employee = await engine.find_one(Employee, Employee.id == id)
        if employee is None:
            raise HTTPException(404)
        return employee

    @classmethod
    async def update_employee(cls, employee: Employee):
        """ Обновление данных сотрудника
        """

        await engine.save(employee)
        return employee

    @classmethod
    async def create_employee(cls, employee: Employee):
        """ Создание сотрудника
        """
        await engine.save(employee)
        return 'ok'

    @classmethod
    async def delete_employee(cls, employee: Employee):
        """ Удаление сотрудника
        """
        try:
            await engine.delete(employee)
            return f'{employee.name} удален!'
        except Exception as e:
            raise HTTPException(404, e)

    @classmethod
    async def search(cls, **kwargs):
        """ Поиск по параметрам

            Ищет только по 1 параметру

            приоритет поиска:
            - имя
            - email
            - company
            - age
            - диапазон возраста
            - диапазон зарплат

        """

        match kwargs:
            case kwargs if kwargs.get('name'):
                result = await engine.find(
                    Employee, query.match(Employee.name,
                                          re.compile(
                                              f"{kwargs['name']}")), )

            case kwargs if kwargs.get('email'):
                result = await engine.find(
                    Employee, query.match(Employee.email,
                                          re.compile(f"{kwargs['email']}")))

            case kwargs if kwargs.get('company'):
                result = await engine.find(
                    Employee, query.match(Employee.company,
                                          re.compile(
                                              f"{kwargs['company']}")))

            case kwargs if kwargs.get('age'):
                result = await engine.find(Employee,
                                           Employee.age == kwargs['age'])

            case kwargs if (kwargs.get('age_min') or kwargs.get('age_max')):
                result = await engine.find(
                    Employee,
                    (Employee.age >= kwargs.get('age_min', 0)) &
                    (Employee.age <= kwargs.get('age_max', 100)),
                    sort=Employee.age, )

            case kwargs if (
                    kwargs.get('salary_min') or kwargs.get('salary_max')):
                result = await engine.find(
                    Employee,
                    (Employee.salary >= kwargs.get('salary_min', 0)) &
                    (Employee.salary <= kwargs.get('salary_max', 1000000)),
                    sort=Employee.salary, )
            case _:
                result = []

        return result
