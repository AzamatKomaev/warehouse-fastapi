from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from auth.hashing import get_password_hash
from . import models
from . import schemas


def register_new_user(db: Session, request) -> models.User:
    new_user = models.User(name=request.name, password=get_password_hash(request.password), type=request.type)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session) -> schemas.UserList:
    users = db.query(models.User).all()
    return schemas.UserList(__root__=users)


def get_user_by_id(db: Session, user_id: int) -> schemas.UserSingle:
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cannot find any user with such data!')
    return schemas.UserSingle(**user.__dict__)

