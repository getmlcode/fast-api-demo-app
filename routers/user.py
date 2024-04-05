from fastapi import (
    Depends,
    status,
    APIRouter)
import schema, database
from sqlalchemy.orm import Session

from models import *
from repository import userRepository


router = APIRouter(
    tags=['users']
)


@router.post('/user/create', status_code=status.HTTP_201_CREATED, response_model=WebResponse.CreateUserResponse)
def create_user(user: User.User, db: Session = Depends(database.get_db)):
    new_user = userRepository.create_user(user, db)
    
    return new_user


@router.post('/user/{id}', status_code=status.HTTP_200_OK, response_model=WebResponse.CreateUserResponse)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = userRepository.get_user(id, db)

    return user