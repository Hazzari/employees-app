from typing import List
from typing import Optional

from fastapi import APIRouter, Query, status
from odmantic import ObjectId

from app.crud.employee import EmployeeCRUD
from app.model.employee import Employee

router = APIRouter()


@router.get("/employee/search", tags=["Search"])
async def search_employees(
        age: Optional[int] = Query(0, ge=0, description='Возраст'),
        age_min: Optional[int] = Query(16, description='Минимальный возраст'),
        age_max: Optional[int] = Query(90, description='Максимальный возраст'),
):
    return await EmployeeCRUD.filter(age_min=age_min,
                                     age=age,
                                     age_max=age_max,
                                     )


@router.get("/employee/", response_model=List[Employee], tags=["Search"])
async def get_employees():
    return await EmployeeCRUD.get_employees()


@router.get("/employee/count/", response_model=int, tags=["Data"])
async def count_employees():
    return await EmployeeCRUD.count_employees()


@router.get("/employee/{id}", response_model=Employee, tags=["CRUD"])
async def get_employee_by_id(id: ObjectId):
    return await EmployeeCRUD.get_employee_by_id(id)


@router.put("/employee/", response_model=Employee, tags=["CRUD"])
async def update_employee(employee: Employee):
    return await EmployeeCRUD.update_employee(employee)


@router.post("/employee/",
             status_code=status.HTTP_201_CREATED,
             response_model=Employee,
             tags=["CRUD"])
async def update_employee(employee: Employee):
    return await EmployeeCRUD.create_employee(employee)


@router.delete("/employee/", response_model=Employee, tags=["CRUD"])
async def update_employee(employee: Employee):
    return await EmployeeCRUD.delete_employee(employee)
