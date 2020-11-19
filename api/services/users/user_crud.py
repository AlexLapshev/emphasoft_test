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
    def update_user_by_email(email: str,
                             first_name: str,
                             last_name: str,
                             patronymic: str,
                             hashed_password: str):
        logger.debug(f'updating user with email: {email}')
        User.update(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            hashed_password=hashed_password,
            active=True).where(User.email == email).execute()

    @staticmethod
    def get_all_users() -> List[UserSchema]:
        logger.debug('getting all users in database')
        users = User.select().where(User.active).execute()
        return [UserSchema.from_orm(user) for user in users]

    @staticmethod
    def create_user(email):
        return User.create(email=email)
