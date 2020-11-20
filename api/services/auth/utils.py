from datetime import datetime
from pathlib import Path

from fastapi import File
from loguru import logger

from api.config.main import main_config
from api.services.users.schemas import UserSchema


class ImageUpload:

    destination_dir = main_config.image_path

    def __init__(self, image: File):
        self.image = image

    async def save_image(self, user: UserSchema):
        logger.debug(f'saving avatar of user with id: {user.user_id}')
        image_extension = self.image.filename.split('.')[-1]
        image = await self.image.read()
        path = Path(__file__).parent.parent.parent.parent
        path = Path(path / self.destination_dir / f'user_id_{str(user.user_id)}')
        path.mkdir(parents=True, exist_ok=True)
        user_image_name = f'user_id_{user.user_id}_{datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S")}.{image_extension}'
        path = path / user_image_name
        with open(path, "wb") as img:
            img.write(image)
        # return Path(f'user_id_{str(user.user_id)}') / user_image_name
        return path
