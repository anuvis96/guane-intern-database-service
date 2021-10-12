from tortoise import Model
from datetime import datetime
from tortoise import fields


class Dog(Model):
    id = fields.IntField(pk=True, index=True)
    dog_name = fields.CharField(max_length=12, null=False, unique=True)
    picture = fields.CharField(
        max_length=200, null=False, default="picture_dog_1.jpg")
    is_adopted = fields.BooleanField(null=False)
    create_date = fields.DatetimeField(default=datetime.utcnow)
    id_user = fields.ForeignKeyField("models.User", related_name="user")
