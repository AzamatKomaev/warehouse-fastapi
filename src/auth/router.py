from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from src.users.models import User
from src.core.database import get_db
from . import hashing
from .jwt import create_access_token
from .schemas import Login


router = APIRouter()


@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={'id': user.id, 'sub': user.name})

    return {"access_token": access_token, "token_type": "bearer"}
