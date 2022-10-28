from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from auth.hashing import get_password_hash
from core.logging import logger


async def register_new_user(db: Session, request) -> models.User:
    new_user = models.User(name=request.name, password=get_password_hash(request.password), type=request.type)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_all_users(db: Session) -> schemas.UserList:
    users = db.query(models.User).all()
    logger.info(*users)
    return schemas.UserList(__root__=users)
