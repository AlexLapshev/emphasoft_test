import base64

from fastapi import File
from loguru import logger

from api.config.main import main_config


class ImageUpload:

    destination_dir = main_config.image_path

    def __init__(self, image: File):
        self.image = image

    async def save_image(self):
        logger.debug('endcoding image')
        encoded_string = base64.b64encode(await self.image.read())
        return encoded_string
