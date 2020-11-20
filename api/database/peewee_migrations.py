from playhouse.migrate import *

from api.database.peewee_connection import db

migrator = PostgresqlMigrator(db)

with db.atomic():
    migrate(
        migrator.alter_column_type('users', 'avatar', TextField(null=True))
    )
