from typing import Optional

from pydantic import BaseModel

from api.database.utils import PeeweeGetterDict


class GoogleAccessTokenSchema(BaseModel):
    access_token: str


class UserSerialized(BaseModel):
    user_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    patronymic: Optional[str]
    avatar: Optional[str]
    active: bool

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserSchema(UserSerialized):
    email: str
    hashed_password: Optional[str]
