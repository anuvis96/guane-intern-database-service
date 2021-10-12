from typing import Any, Dict, List, TypeVar, Union

from pydantic import BaseModel
from tortoise import models
from app.crud.base import ICrudBase, ModelType, CreateSchemaType, UpdateSchemaType


class CRUDBase(ICrudBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    async def get_by_name(self, *, name: str) -> Union[dict, None]:
        model = await self.model.filter(name=name).first().values()
        if model:
            return model[0]
        return None

    async def get_all(
        self,
        *,
        payload: dict = None,
        skip: int = 0,
        limit: int = 10,
    ) -> List:
        if payload:
            model = (
                await self.model.filter(**payload)
                .offset(skip)
                .limit(limit)
                .all()
                .values()
            )
        else:
            model = await self.model.all().offset(skip).limit(limit).values()
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> Union[dict, None]:
        obj_in_data = obj_in.dict()
        model = self.model(**obj_in_data)
        await model.save()
        return model

    async def update(self, *, name: str, obj_in: Dict[str, Any]) -> Union[dict, None]:
        if not obj_in:
            model = await self.model.filter(name=name).first().values()
        else:
            model = await self.model.filter(name=name).update(**obj_in)
        if model:
            update_model = await self.model.filter(name=name).first().values()
            model_m = self.model(**update_model[0])
            update_fields = list(update_model[0].keys())
            await model_m.save(update_fields=update_fields)
            return update_model[0]
        return None

    async def delete(self, *, name: str) -> int:
        model = await self.model.filter(name=name).first().delete()
        return model
