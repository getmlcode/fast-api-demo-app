from fastapi import HTTPException, status
import schema
from sqlalchemy.orm import Session
from models import Blog


def create_blog(blog: Blog.Blog, db: Session):
    new_blog = schema.Blog(title=blog.title, 
                           body=blog.body, 
                           published=blog.published,
                           user_id = 1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


def get_blog(id: int, db: Session):
    blog = db.query(schema.Blog).filter(schema.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details':f'Blog with id {id} is not available in database'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not available in database')
    return blog


def get_all_blogs(db: Session):
    return db.query(schema.Blog).all()


def remove_blog(id, db: Session ):
    blog = db.query(schema.Blog).filter(schema.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not available in database')
    
    blog.delete(synchronize_session=False)
    db.commit()

    return 'Blog deleted successfully'


def update_blog(id, updated_blog: Blog.Blog, db: Session):
    blog = db.query(schema.Blog).filter(schema.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not available in database')
    
    blog.update({schema.Blog.body:updated_blog.body,
                 schema.Blog.title:updated_blog.title,
                 schema.Blog.published:updated_blog.published}, 
                 synchronize_session=False)

    db.commit()

    return f'blog with id={id}, updated successfully'