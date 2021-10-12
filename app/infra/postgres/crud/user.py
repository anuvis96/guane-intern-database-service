from pydantic.main import Model
from crud.base import CRUDBase
from app.models.user import User
from typing import Any, Dict, List, TypeVar, Union
from app.schemas.user_schema import In_User_Schema, Out_User_Schema


class UserCrud(CRUDBase[User, In_User_Schema, Out_User_Schema]):
    ...
async def get_by_id(self, *, id: int) -> Union[dict, None]:
        model = await self.model.filter(id=id).first().values()
        if model:
            return model[0]
        return None


async def delete_id(self, *, id: int) -> int:
        model = await self.model.filter(id=id).first().delete()
        return model        
  
user_crud = UserCrud(Model=User)