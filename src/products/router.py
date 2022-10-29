from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import schemas, services


router = APIRouter()


@router.get('/', response_model=schemas.ProductList)
def get_all_products(db: Session = Depends(get_db)):
    return services.get_products_list(db)


@router.post('/add', response_model=schemas.ProductSingle)
def add_product(item: schemas.ProductCreate, db: Session = Depends(get_db)):
    pass


@router.get('/{product_id}', response_model=schemas.ProductSingle)
def get_detail_product(product_id: int, db: Session = Depends(get_db)):
    pass


@router.post('/{product_id}/buy', response_model=schemas.ProductSingle)
def buy_product(product_id: int, db: Session = Depends(get_db)):
    pass
