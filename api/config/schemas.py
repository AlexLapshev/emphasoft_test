from pydantic import BaseSettings, PostgresDsn
from typing import List


class SettingsDB(BaseSettings):
    postgres_url: PostgresDsn
    postgres_host: str
    postgres_port: int
    postgres_name: str
    postgres_user: str
    postgres_password: str


class SettingsFront(BaseSettings):
    front_app_url: str


class SettingsApp(BaseSettings):
    origins: List[str]
    reload: bool = False
    host: str
    port: int
    workers: int
    secret_key: str
    image_path: str


class SettingsGoogle(BaseSettings):
    google_client_id: str
    google_client_secret: str
    google_api_key: str


class Settings(SettingsDB, SettingsFront, SettingsApp, SettingsGoogle):
    pass



