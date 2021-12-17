from dataclasses import dataclass

from fastapi import APIRouter, HTTPException
from odmantic import ObjectId, query

from app.database.database import engine
from app.model.employee import Employee
from app.utils.serializer_search import serializes_search_params

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
        return await engine.save(employee)

    @classmethod
    async def delete_employee(cls, id: str):
        """ Удаление сотрудника
        """
        emp = await engine.find_one(Employee, Employee.id == ObjectId(id))
        if emp is None:
            raise HTTPException(404, 'Employee not found')
        await engine.delete(emp)
        return f'{emp.name} удален!'

    @classmethod
    async def search(cls, **kwargs):
        """ Поиск по параметрам
        """
        result = serializes_search_params(kwargs)
        if not result:
            raise HTTPException(404, 'Parameters not passed')
        return await engine.find(Employee, query.and_(*result))
