from core.hashing import Hasher
from db.base import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session) -> User:
    new_user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
