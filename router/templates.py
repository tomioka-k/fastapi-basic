from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from schemas import ProductBase


router = APIRouter(
    prefix='/templates',
    tags=['templates']
)

templates = Jinja2Templates(directory='templates')

@router.get("/products/{id}", response_class=HTMLResponse)
def get_product(id: str, request: Request):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id
        }
    )

@router.post("/products/{id}", response_class=HTMLResponse)
def get_product(id: str, product: ProductBase ,request: Request):
    return templates.TemplateResponse(
        "product_post.html",
        {
            "request": request,
            "id": id,
            "product": product
        }
    )