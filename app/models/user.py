from tortoise import Model, fields
from datetime import datetime


class User(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=12, null=False)
    last_name = fields.CharField(max_length=12, null=False)
    email = fields.CharField(max_length=200, null=False)
    password = fields.CharField(max_length=8, null=True)
    create_date = fields.DatetimeField(default=datetime.utcnow)
