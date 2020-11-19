from playhouse.migrate import *

from api.database.peewee_connection import db

migrator = PostgresqlMigrator(db)

with db.atomic():
    migrate(
        migrator.add_column('users', 'hashed_password',
                            CharField(max_length=255, null=True)
                            )
    )
