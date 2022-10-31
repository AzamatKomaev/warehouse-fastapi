from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    count: int


class ProductCreate(ProductBase):
    pass


class ProductSingle(ProductBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ProductList(BaseModel):
    __root__: List[ProductSingle]


class UserCartSingle(BaseModel):
    id: int
    user_id: int
    product_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

