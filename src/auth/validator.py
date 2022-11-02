from typing import Optional
from sqlalchemy.orm import Session
from .models import User


def verify_name_exist(db: Session, name: str) -> Optional[User]:
    return db.query(User).filter(User.name == name).first()
