import uvicorn
from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from api.config.main import main_config
from api.database.peewee_connection import db
from api.middleware.authentication_middleware import BasicAuthBackend, on_auth_error
from api.services.auth.router import security
from api.services.users.models import User
from api.services.users.router import users

db.connect()
db.create_tables([User])
db.close()


def create_app():
    app: FastAPI = FastAPI(debug=True)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=main_config.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(AuthenticationMiddleware,
                       backend=BasicAuthBackend(),
                       on_error=on_auth_error
                       )
    app.include_router(users, prefix='/api/v1/users', tags=['users'])
    app.include_router(security, prefix='/api/v1/security', tags=['security'])
    return app


app = create_app()


if __name__ == "__main__":

    uvicorn.run('api.main:app', host=main_config.host, port=main_config.port,
                reload=main_config.reload, workers=main_config.workers)
