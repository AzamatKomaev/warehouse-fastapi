from typing import Optional
from pydantic import BaseModel


class Login(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TokenData(BaseModel):
    id: int
    name: Optional[str] = None
