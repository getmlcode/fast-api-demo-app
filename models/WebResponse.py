from pydantic import BaseModel
from typing import Optional, List


class BlogBase(BaseModel):
    title: str
    body: str

class UserBlog(BlogBase):
    class Config:
        orm_mode = True

class CreateUserResponse(BaseModel):
    name: str
    email: str
    blogs: List[UserBlog]
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    creator: CreateUserResponse

    class Config:
        orm_mode = True