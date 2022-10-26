from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from src.auth.hashing import get_password_hash
from src.core.logging import logger


async def register_new_user(db: Session, request) -> models.User:
    new_user = models.User(name=request.name, password=get_password_hash(request.password), type=request.type.value)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_all_users(db: Session) -> schemas.UserList:
    users = db.query(models.User).all()
    return schemas.UserList(__root__=users)


def get_detail_user(db: Session, id: int):
    user = db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="Data Not Found !")

    return schemas.UserSingle(**user.__dict__)
