from typing import List

from fastapi import APIRouter
from odmantic import ObjectId

from app.crud.user import UserCRUD
from app.model.user import User

router = APIRouter()


@router.get("/user/", response_model=List[User], tags=["API User"])
async def get_users():
    return await UserCRUD.get_users()


@router.get("/user/count", response_model=int, tags=["Дополнительно"])
async def count_users():
    return await UserCRUD.count_users()


@router.get("/user/{id}", response_model=User, tags=["Дополнительно"])
async def get_user_by_id(id: ObjectId):
    return await UserCRUD.get_user_by_id(id)


@router.put("/user/", response_model=User, tags=["Дополнительно"])
async def update_user(user: User):
    return await UserCRUD.update_user(user)
