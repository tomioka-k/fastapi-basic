from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import Article
from fastapi import HTTPException, status

def create_article(db: Session, request: ArticleBase):
    new_article = Article(
        title = request.title,
        content = request.content,
        is_display = request.is_display,
        creater_id = request.creater_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id).first()
    return article