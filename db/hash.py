from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def get_password_hash(password: str):
        return pwd_cxt.hash(password)

    def verify_password(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)