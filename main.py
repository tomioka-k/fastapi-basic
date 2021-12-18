from typing import Optional, List
from fastapi import FastAPI, Header, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from router import articles, users, products
from auth import authentication
from db import models
from db.database import engine

app = FastAPI()
app.include_router(articles.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(authentication.router)

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

@app.get('/cookie')
def save_cookie(response: Response):
    response.set_cookie(key="sample_cookie", value="sample_cookie_value")
    return "ok"

@app.get('/cookie2')
def get_cookie(sample_cookie: Optional[str] = Cookie(None)):
    return {
        "sample_cookie": sample_cookie
    }

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
