import enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from core.logging import logger


class UserTypeEnum(enum.Enum):
    seller = 'seller'
    buyer = 'buyer'


class UserBase(BaseModel):
    name: str
    type: UserTypeEnum

    class Config:
        use_enum_values = True


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserSingle(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserList(BaseModel):
    __root__: List[UserSingle]


class Login(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TokenData(BaseModel):
    id: int
    name: Optional[str] = None

