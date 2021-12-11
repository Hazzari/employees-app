from dataclasses import dataclass

from fastapi import APIRouter
from fastapi import HTTPException
from odmantic import ObjectId

from app.database.database import engine
from app.model.user import User

router = APIRouter()


@dataclass
class UserCRUD:
    model = User

    @classmethod
    async def get_users(cls):
        document = await engine.find(cls.model)
        return document

    @classmethod
    async def count_users(cls):
        count = await engine.count(cls.model)
        return count

    @classmethod
    async def get_user_by_id(cls, id: ObjectId):
        user = await engine.find_one(User, User.id == id)
        if user is None:
            raise HTTPException(404)
        return user

    @classmethod
    async def update_user(cls, user: User):
        await engine.save(user)
        return user
