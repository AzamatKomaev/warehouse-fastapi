from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from src.auth.models import User
from src.core.database import get_db
from . import services, hashing, schemas, validator
from .jwt import create_access_token


router = APIRouter()


@router.get('/users', response_model=schemas.UserList)
async def get_all_users(db: Session = Depends(get_db)):
    return await services.get_all_users(db)


@router.get('/users/{id}')
async def get_detail_user(id: int, db: Session = Depends(get_db)):
    return await services.get_detail_user(db, id)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user = await validator.verify_name_exist(db, request.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this name already exists in the system.",
        )

    new_user = await services.register_new_user(db, request)
    return new_user


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={'id': user.id, 'sub': user.name})

    return {"access_token": access_token, "token_type": "bearer"}
