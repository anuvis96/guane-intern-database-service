from pydantic import BaseModel
from datetime import datetime


class In_User_Schema(BaseModel):
    # Clase pydantic = convertida a python
    name: str
    last_name: str
    email: str
    password: str
    create_date: datetime


class Out_User_Schema(BaseModel):
    id: int
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True
