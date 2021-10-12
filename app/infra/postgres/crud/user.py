from pydantic.main import Model
from crud.base import CRUDBase
from app.models.user import User
from typing import Any, Dict, List, TypeVar, Union
from app.schemas.user_schema import In_User_Schema, Out_User_Schema


class UserCrud(CRUDBase[User, In_User_Schema, Out_User_Schema]):
    ...       
  
user_crud = UserCrud(Model=User)