from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status)
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from models import Login, Token, TokenData
import database, schema
from hashing import Hash
import JWTtoken

router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(schema.User).filter(schema.User.email==request.username).first()

    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details':f'Blog with id {id} is not available in database'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'User with username={request.username} does not exist')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Incorrect password')
    
    # Generate JWT
    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    #print(access_token)
    
    return {"access_token":access_token, "token_type":"bearer"}