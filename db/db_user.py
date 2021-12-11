from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import User


def create_user(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()