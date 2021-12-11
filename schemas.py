from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str

class ArticleCreate(ArticleBase):
    is_display: bool


class ArticleDisplay(ArticleBase):
    id: int
    class Config():
        orm_mode = True


