import enum
from sqlalchemy import String, DateTime, Integer, Enum
from sqlalchemy.sql import func
from src.core.database import Base
from src.core.utils import Column


class UserTypeEnum(enum.Enum):
    """Type of users. User can be seller or buyer."""
    seller = 'seller'
    buyer = 'buyer'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    type1 = Column(Enum(UserTypeEnum))
    password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User(name={self.name} type={self.type1}>'

