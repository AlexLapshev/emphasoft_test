from fastapi import Depends, HTTPException, APIRouter, Form, File
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger

from api.services.auth.schemas import TokenSchema
from api.services.auth.user_auth import authenticate_user
from starlette.responses import JSONResponse

from api.services.auth.jwt_work import create_access_token
from api.database.peewee_connection import get_db
from api.services.users.schemas import GoogleAccessTokenSchema
from api.services.users.user_crud import UserCRUD
from api.services.users.utils import check_google_id

security = APIRouter()
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30


@security.post("/login", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                conn=Depends(get_db)) -> JSONResponse:
    if user := authenticate_user(form_data.username, form_data.password):
        logger.debug('authenticating user {}'.format(user.email))
        if user.active:
            access_token = create_access_token(
                data={"sub": user.email}
            )
            return JSONResponse(content={"access_token": access_token,
                                         "token_type": "bearer", }, status_code=200)
    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@security.post('/google-auth')
async def google_auth(access_info: GoogleAccessTokenSchema):
    user_email = check_google_id(access_info.access_token)['email']
    if user := UserCRUD.get_user_by_email(user_email):
        if user.active:
            access_token = create_access_token(
                data={"sub": user.email}
            )
            return JSONResponse(content={"access_token": access_token,
                                         "token_type": "bearer", }, status_code=200)
    else:
        UserCRUD.create_user(user_email)
    raise HTTPException(status_code=403, detail='inactive user')


@security.post('/register')
async def register(first_name: str = Form(...),
                   last_name: str = Form(...),
                   password: str = Form(...),
                   patronymic: str = Form(...),
                   avatar: bytes = File(...),
                   ):
    return JSONResponse(status_code=200, content='success')
