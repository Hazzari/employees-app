from typing import List
from typing import Optional

from fastapi import APIRouter, Query, status
from odmantic import ObjectId

from app.crud.employee import EmployeeCRUD
from app.model.employee import Employee

router = APIRouter()


@router.get("/employee/", response_model=List[Employee], tags=["All"])
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


@router.get("/employee/search/", tags=["Search"])
async def search_employees(
        name: Optional[str] = Query(None, description='Имя'),
        company: Optional[str] = Query(None, description='Компания'),
        email: Optional[str] = Query(None, description='Email'),
        age: Optional[int] = Query(None, description='Возраст'),
        age_min: Optional[int] = Query(
            None, description='Минимальный возраст'),
        age_max: Optional[int] = Query(
            None, description='Максимальный возраст'),
        salary_min: Optional[int] = Query(
            None, description='Минимальная зарплата'),
        salary_max: Optional[int] = Query(
            None, description='Максимальная зарплата'),
):
    request_search_params = {
        "age": age,
        'age_min': age_min,
        'age_max': age_max,
        'name': name,
        'email': email,
        'company': company,
        'salary_min': salary_min,
        'salary_max': salary_max,
    }

    return await EmployeeCRUD.search(
        **{x: k for x, k in request_search_params.items()
           if k is not None}
    )
