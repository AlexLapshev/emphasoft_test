from typing import List

from fastapi import APIRouter, Depends, Form, File
from starlette.responses import JSONResponse

from api.services.auth.user_auth import get_current_active_user
from api.services.users.schemas import UserSerialized
from api.services.users.user_crud import UserCRUD

users = APIRouter()


@users.get('/all', response_model=List[UserSerialized])
async def all_users(current_user=Depends(get_current_active_user)):
    return UserCRUD.get_all_users()
