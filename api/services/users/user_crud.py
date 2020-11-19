from typing import List

from loguru import logger

from api.services.users.models import User
from api.services.users.schemas import UserSchema


class UserCRUD:

    @staticmethod
    def get_user_by_email(email: str) -> UserSchema:
        if user := User.get_or_none(User.email == email):
            logger.debug(f'user found by email: {user.email}')
            return UserSchema.from_orm(user)

    @staticmethod
    def get_all_users() -> List[UserSchema]:
        logger.debug('getting all users in database')
        users = User.select().execute()
        return [UserSchema.from_orm(user) for user in users]

    @staticmethod
    def create_user(email):
        pass
