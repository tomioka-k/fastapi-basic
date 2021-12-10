from fastapi import APIRouter

router = APIRouter(
    prefix='/article',
    tags=['article']
)

@router.get('/all')
def get_all_articles():
    return {'message': f'All articles'}

@router.get('/{id}')
def get_article(id: int):
    return {'message': f'Blog is {id}'}