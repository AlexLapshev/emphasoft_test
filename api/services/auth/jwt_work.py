import logging

from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt, JWTError, ExpiredSignatureError
from loguru import logger
from typing import Optional

from api.config.main import main_config

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
                        secret_key=main_config.secret_key) -> str:
    logging.debug('creating access token')
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm='HS512')
    return encoded_jwt


def decode_token(token, secret_key=main_config.secret_key):
    logging.debug('decoding token')
    try:
        decoded_jwt = jwt.decode(token, secret_key, algorithms=['HS512'])
        return decoded_jwt
    except ExpiredSignatureError as e:
        logger.debug('expired token')
        raise HTTPException(status_code=401, detail="token has expired")
    except JWTError as e:
        logger.debug('invalid token')
        raise HTTPException(status_code=401, detail="invalid basic auth credentials")
