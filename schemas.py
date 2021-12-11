from typing import List
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str
    is_display: bool
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    articles: List[Article] = []
    class Config():
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    content: str
    is_display: bool
    creater_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    is_display: bool
    user: User
    class Config():
        orm_mode = True