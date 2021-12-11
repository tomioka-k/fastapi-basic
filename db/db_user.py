from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserCreate
from db.models import User


def create_user(db: Session, request: UserCreate):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user