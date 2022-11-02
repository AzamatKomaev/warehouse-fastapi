from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from auth.models import User
from core.database import get_db
from . import (
    services,
    hashing,
    schemas,
    validator,
    jwt
)


router = APIRouter()


@router.get('/users', response_model=schemas.UserList)
def get_all_users(db: Session = Depends(get_db)):
    return services.get_all_users(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_user_registration(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user = validator.verify_name_exist(db, request.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this name already exists in the system.",
        )

    new_user = services.register_new_user(db, request)
    return new_user


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = jwt.create_access_token(data={'id': user.id, 'sub': user.name})

    return {"access_token": access_token, "token_type": "bearer"}
