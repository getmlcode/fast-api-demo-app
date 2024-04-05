from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash:
    @classmethod
    def bcrypt(cls, password: str):
        return pwd_ctx.hash(password)
    
    @classmethod
    def verify(cls, plain_pwd: str, hashed_pwd: str):
        return pwd_ctx.verify(plain_pwd, hashed_pwd)