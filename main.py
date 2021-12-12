from fastapi import FastAPI
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

models.Base.metadata.create_all(engine)