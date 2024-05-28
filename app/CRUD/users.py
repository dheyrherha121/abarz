from fastapi import FastAPI,APIRouter,HTTPException
from .. import schema

router = APIRouter(
    prefix= 'users/',
    tags=['user']
)

@router('/')
def CreateUser(user:schema.UserIn):
    return user