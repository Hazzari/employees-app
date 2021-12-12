from dataclasses import dataclass

from fastapi import APIRouter, HTTPException
from odmantic import ObjectId

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
    async def filter(cls, age_min: int, age: int, age_max: int):
        """ Фильтрация по возрасту.
                    Или по точному указанию, либо по диапазону.

            :param age: Фильтрация по возрасту.
            :param age_min: Фильтрация по минимальному возрасту.
            :param age_max: Фильтрация по максимальному возрасту.
            :return: {list} Найденные пользователи. Отсортированные по возрастанию.
            """
        if age:
            result = await engine.find(Employee, Employee.age == age)
        else:
            result = await engine.find(
                Employee,
                (Employee.age >= age_min) & (Employee.age <= age_max),
                sort=Employee.age,
            )
        return result
