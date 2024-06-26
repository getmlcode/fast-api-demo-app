from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import JWTtoken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):

    return JWTtoken.verify_token(token)

