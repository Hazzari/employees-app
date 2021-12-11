from fastapi import APIRouter

router = APIRouter()


@router.get('/user')
async def get_user():
    return {'user': 123}


@router.get('/user{_id}')
async def create_user(_id):
    return _id


@router.post('/user')
async def create_user(user):
    return user


@router.put('/user{_id}')
async def update_user(_id):
    return _id


@router.delete('/user{_id}')
async def delete_user(_id):
    return _id
