from contextvars import ContextVar

import peewee

from fastapi import Depends
from loguru import logger

from api.config.main import main_config

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(database=main_config.postgres_name, user=main_config.postgres_user,
                               password=main_config.postgres_password,
                               host=main_config.postgres_host, port=main_config.postgres_port)


db._state = PeeweeConnectionState()


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        logger.debug('connect to postgres')
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
