from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from auth.schemas import UserSingle
from . import models, schemas


def is_user_seller(user: UserSingle) -> bool:
    """Check is user a buyer."""
    return user.type == 'seller'


def get_product_by_id(db: Session, product_id: int) -> models.Product:
    """Get any product by id. If product was not found raise exception. """
    product = db.query(models.Product).get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cannot find any product with such data!')
    return product


def get_products_list(db: Session) -> List[models.Product]:
    products = db.query(models.Product).all()
    return products


def add_product(db: Session, item: schemas.ProductCreate, user_id: int) -> models.Product:
    product = models.Product(**item.dict(), user_id=user_id)
    db.add(product)
    db.flush()
    db.commit()
    db.refresh(product)
    return product


def buy_product(db: Session, user_id: int, product_id: int) -> models.UserCart:
    """Buy any product by only users with type buyer. Return user cart with product_id and user_id."""
    product = get_product_by_id(db, product_id)

    if product.count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no more items of the product')

    cart = models.UserCart(user_id=user_id, product_id=product_id)
    product.count -= 1
    db.add(cart)
    db.commit()
    db.refresh(product)
    return cart
