from fastapi import HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token
from loguru import logger

from api.config.main import main_config


def check_google_id(token: str) -> dict:
    logger.debug('validating google id')
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), main_config.google_client_id)
        return id_info
    except ValueError:
        raise HTTPException(status_code=403, detail='invalid google id_token')
