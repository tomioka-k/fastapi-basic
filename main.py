from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return 'Hello World'

class ArticleModel(BaseModel):
    title: str
    content: str
    username: str
    tag: List[str] = []
    metadata: Dict[str, str] = {'key': 'value'}

@app.post('/article')
def get_article(article: List[ArticleModel], username: Optional[str] = None, is_display: bool = True):
    return {
        'article': article,
        'username': username,
        'is_display': is_display
    }

@app.get('/article/all')
def get_article(username: Optional[str] = None, is_display: bool = True):
    return {'message': f'article all query {username} and {is_display}'}

@app.get('/article/{id}')
def get_article(id: int): 
    return {'message': f'article is {id}'}

@app.get('/article/{id}/comments/{comment_id}')
def get_article(id: int, comment_id: int):
    return {'message': f'article is {id} and {comment_id}'}