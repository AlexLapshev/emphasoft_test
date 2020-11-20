from api.services.users.user_crud import UserCRUD

from jose import JWTError, ExpiredSignatureError
from loguru import logger
from passlib.context import CryptContext


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from api.services.auth.jwt_work import decode_token
from api.services.auth.schemas import TokenDataSchema
from api.database.peewee_connection import get_db
from api.services.users.schemas import UserSchema

pwd_context = CryptContext(schemes=["sha512_crypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/security/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str) -> UserSchema or None:
    logger.debug('authenticating user')
    user = UserCRUD.get_user_by_email(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return
    return user


def get_current_user(token: str = Depends(oauth2_scheme), dependencies=[Depends(get_db)]) -> UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenDataSchema(email=email)
    except ExpiredSignatureError as exc:
        raise HTTPException(status_code=401, detail="Expired token", headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise credentials_exception
    user = UserCRUD.get_user_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: UserSchema = Depends(get_current_user)) -> UserSchema:
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
