from typing import List
from sqlalchemy.orm import Session
from core.logging import logger
from . import models, schemas


def get_products_list(db: Session) -> List[models.Product]:
    products = db.query(models.Product).all()
    logger.info(type(products))
    return products


def add_product(db: Session, item: schemas.ProductCreate) -> models.Product:
    product = models.Product(**item.dict())
    db.add(product)
    db.flush()
    db.commit()
    db.refresh(product)
    return product

