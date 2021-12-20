from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import Response, HTMLResponse
import time

router = APIRouter(
    prefix='/products',
    tags=['products']
)

products = ['water', 'cola', 'coffee']

async def time_consuming_functionality(sec: int = 5):
    time.sleep(sec)
    return 'ok'

@router.get('/all')
async def get_products_all():
    await time_consuming_functionality()
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