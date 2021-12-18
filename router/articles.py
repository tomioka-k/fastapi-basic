from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from schemas import ArticleBase, ArticleDisplay
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)

@router.post('/', response_model=ArticleDisplay)
def create_article(
    request: ArticleBase, 
    db: Session = Depends(get_db), 
    current_user: str = Depends(get_current_user)
    ):
    return db_article.create_article(db, request)

@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    article = db_article.get_article(db, id)
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {id} not found"
            )
    return article