from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.sql import func
from core.database import Base
from core.utils import Column


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    count = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Product(name={self.name} count={self.count} user_id={self.user_id})'


class UserCart(Base):
    __tablename__ = 'users_carts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<UserCart(user_id={self.user_id} product_id={self.product_id})'
