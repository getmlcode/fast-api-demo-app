from fastapi import HTTPException, status
import schema
from sqlalchemy.orm import Session
from models import User
from hashing import Hash


def create_user(user: User.User, db: Session):
    new_user = schema.User(name=user.name, 
                           email=user.email, 
                           password=Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def get_user(id: int, db: Session):
    user = db.query(schema.User).filter(schema.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'User with id {id} is not available in database')

    return user