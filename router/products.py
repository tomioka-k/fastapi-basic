from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import Response, HTMLResponse
from sqlalchemy.util.langhelpers import set_creation_order

router = APIRouter(
    prefix='/products',
    tags=['products']
)

products = ['water', 'cola', 'coffee']

@router.get('/all')
def get_products_all():
    text_data = " ".join(products)
    return Response(content=text_data, media_type='text/plain', status_code=status.HTTP_200_OK)

@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>product is id</div>"
            }
        },
        "description": "return html object"
    }
})
def get_product(id: int):
    product = products[id]
    html = f"""
        <html>
            <h2>product is {id}</h2>
        </html>
    """
    return HTMLResponse(content=html, media_type="text/html", status_code=status.HTTP_200_OK)