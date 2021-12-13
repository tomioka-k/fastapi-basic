from typing import Optional, List
from fastapi import FastAPI, Header, Response
from router import articles, users, products
from db import models
from db.database import engine

app = FastAPI()
app.include_router(articles.router)
app.include_router(users.router)
app.include_router(products.router)

@app.get('/hello')
def index():
    return 'Hello World'

@app.get('/header')
def custom_header(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)
    ):
    response.headers['custom_response_header'] = ". ".join(custom_header)
    return f"{custom_header}"

models.Base.metadata.create_all(engine)