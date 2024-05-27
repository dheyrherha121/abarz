from fastapi import FastAPI,APIRouter,HTTPException,
from

router = APIRouter(
    prefix= 'users/',
    tags=['user']
)

@router('/')
def CreateUser(user:)