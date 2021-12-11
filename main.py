from fastapi import FastAPI
from router import articles
from db import models
from db.database import engine

app = FastAPI()
app.include_router(articles.router)

@app.get('/hello')
def index():
    return 'Hello World'

models.Base.metadata.create_all(engine)