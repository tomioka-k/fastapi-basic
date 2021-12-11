from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    articles = relationship("Article", back_populates="user")

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    is_display = Column(Boolean)
    creater_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="articles")