from .database import Base
from sqlalchemy import Column, ForeignKey,Integer,String, VARCHAR
class Products(Base):

    __tablename__ = 'product'

    id= Column(Integer, primary_key=True, nullable=False)
    Title= Column(String, nullable=False)
    Desciption= Column(VARCHAR, nullable=False)
    Price = Column(Integer, nullable=False)

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(VARCHAR, nullable=False, unique=True)
    password = Column(VARCHAR, nullable=False)