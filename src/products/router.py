from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.schemas import TokenData
from auth.services import get_user_by_id
from auth.jwt import get_current_user
from core.database import get_db
from . import schemas, services

router = APIRouter()


@router.get('/', response_model=schemas.ProductList)
def get_all_products(db: Session = Depends(get_db)):
    return services.get_products_list(db)


@router.post('/add', response_model=schemas.ProductSingle, status_code=status.HTTP_201_CREATED)
def add_product(item: schemas.ProductCreate,
                db: Session = Depends(get_db),
                current_user: TokenData = Depends(get_current_user)
                ):
    user = get_user_by_id(db, current_user.id)
    if not services.is_user_seller(user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cannot do that!')
    return services.add_product(db, item, current_user.id)


@router.post('/buy/{product_id}', response_model=schemas.UserCartSingle)
def buy_product(product_id: int,
                db: Session = Depends(get_db),
                current_user: TokenData = Depends(get_current_user)
                ):
    user = get_user_by_id(db, current_user.id)
    if services.is_user_seller(user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cannot do that!')

    return services.buy_product(db, user.id, product_id)
