from fastapi import (
    FastAPI, 
    Depends,
    status,
    APIRouter,
    File,
    UploadFile,
    Body)
from models import *
import database, oauth2
from sqlalchemy.orm import Session
from typing import List, Optional
from repository import blogRepository

import json

router = APIRouter(
    tags=['blogs']
)


@router.post('/blog/create', status_code=status.HTTP_201_CREATED)
def create_blog(blog: Blog.Blog, db: Session = Depends(database.get_db)):
    new_blog =  blogRepository.create_blog(blog, db)
    return new_blog


@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=WebResponse.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    blog = blogRepository.get_blog(id, db)

    return blog


@router.get('/all/blog', response_model=List[WebResponse.ShowBlog], status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(database.get_db), current_user: User.User = Depends(oauth2.get_current_user)):
    return blogRepository.get_all_blogs(db)

# @app.get('/all/blog', response_model=List[WebResponse.ShowBlog], status_code=status.HTTP_200_OK, tags=['blogs'])
# def get_all_blogs(db: Session = Depends(get_db)):
#     all_blogs = db.query(schema.Blog).all()

#     return all_blogs


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_blog(id, db: Session = Depends(database.get_db)):
    return blogRepository.remove_blog(id, db)


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, updated_blog: Blog.Blog, db: Session = Depends(database.get_db)):
    return blogRepository.update_blog(id, updated_blog, db)


@router.post('/blog/upload', status_code=status.HTTP_200_OK)
def upload_multiple_file(files: List[UploadFile], body = Body(...), db: Session = Depends(database.get_db)):
    print(f'{len(files)} files sent for upload')
    print(body)
    print(type(body))
    #body = '{"a": 1, "b": 2}'
    #json_object = json.loads(body)
    #print(f'jsonobj type{type(json_object)}')

    return {'filename':files[0].filename, 'content_type':files[0].content_type}


@router.get('/published/blog')
def get_published_blog(limit: int=3, 
                       published: bool=True, 
                       topic: Optional[str]=""):
    # args are query parameters
    if published:
        return {
            'data': f'{limit} published blogs on {topic} topic'
        }
    else:
        return {
            'data': f'{limit} unpublished blogs on {topic} topic'
        }