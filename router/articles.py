from typing import List
import typing
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm.session import Session
from db import db_article
from db.database import get_db
from db.models import Article
from schemas import ArticleCreate, ArticleDisplay

router = APIRouter(
    prefix='/article',
    tags=['article']
    )

@router.post('/', response_model=ArticleDisplay)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    return db_article.create_article(db, article)

@router.get('/', response_model=List[ArticleDisplay])
def get_articles_all(db: Session = Depends(get_db)):
    return db_article.get_articles_all(db)

@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)

@router.put('/{id}')
def update_article(id: int, request: ArticleCreate, db: Session = Depends(get_db)):
    return db_article.update_article(db, id, request)

@router.delete('/{id}')
def delete_article(id: int, db: Session = Depends(get_db)):
    return db_article.delete_article(db, id)