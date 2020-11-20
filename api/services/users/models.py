import peewee

from api.database.peewee_connection import db


class User(peewee.Model):

    user_id = peewee.BigAutoField(primary_key=True)
    first_name = peewee.CharField(max_length=50, null=True)
    last_name = peewee.CharField(max_length=50, null=True)
    patronymic = peewee.CharField(max_length=50, null=True)
    email = peewee.CharField(max_length=50, unique=True)
    active = peewee.BooleanField(default=False)
    avatar = peewee.TextField(null=True)
    hashed_password = peewee.CharField(max_length=255, null=True)

    class Meta:
        table_name = 'users'
        database = db

    def __repr__(self):
        return f'user_id: {self.user_id}, user_fullname: {self.first_name + " " + self.last_name}'
