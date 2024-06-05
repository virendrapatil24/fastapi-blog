from db.models.user import User
from sqlalchemy.orm import Session


def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter(User.email == email).first()
