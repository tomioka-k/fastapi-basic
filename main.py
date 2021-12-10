from fastapi import FastAPI
from router import articles

app = FastAPI()
app.include_router(articles.router)

@app.get('/hello')
def index():
    return 'Hello World'