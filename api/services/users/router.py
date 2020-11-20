from typing import List

from fastapi import APIRouter, Depends

from api.services.auth.user_auth import get_current_active_user
from api.services.users.schemas import UserSerialized, UserSchema
from api.services.users.user_crud import UserCRUD

users = APIRouter()


@users.get('/all', response_model=List[UserSerialized])
async def all_users(current_user: UserSchema = Depends(get_current_active_user)):
    return UserCRUD.get_all_users()


@users.get('/me', response_model=UserSerialized)
async def me(current_user: UserSchema = Depends(get_current_active_user)):
    return UserCRUD.get_user_by_id(user_id=current_user.user_id)
