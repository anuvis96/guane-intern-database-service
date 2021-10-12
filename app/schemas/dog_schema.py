from pydantic import BaseModel
from datetime import datetime


class Dog_Schema(BaseModel):
    # Clase pydantic = convertida a python
    dog_name: str
    picture: str
    is_adopted: bool
    create_date: datetime
    user: int

    class Config:
        orm_mode = True


class Dog_Schema_Update(BaseModel):
    # Clase pydantic = convertida a python
    dog_name: str
    picture: str
    is_adopted: bool
    create_date: datetime
    user: int

    class Config:
        orm_mode = True
