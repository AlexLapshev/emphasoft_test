import base64

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import FileResponse, JSONResponse

from api.services.auth.user_auth import get_current_active_user
from api.services.users.schemas import UserSchema
from api.services.users.user_crud import UserCRUD

images = APIRouter()


@images.get('')
async def image(user_id: int, current_user: UserSchema = Depends(get_current_active_user)):
    if user := UserCRUD.get_user_by_id(user_id):
        if user.avatar:
            with open(user.avatar, "rb") as image_file:
                encoded_image_string = base64.b64encode(image_file.read())
            ext = user.avatar.split('.')[-1]
            return FileResponse(user.avatar)
    raise HTTPException(status_code=404, detail='image not found')
