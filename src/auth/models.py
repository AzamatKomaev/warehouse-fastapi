from sqlalchemy import String, DateTime, Integer
from sqlalchemy.sql import func
from core.database import Base
from core.utils import Column


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    type = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User(name={self.name} type={self.typese}>'

