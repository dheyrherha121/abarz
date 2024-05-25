from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix= 'Products/',
    tags= ['Product']
)

@router('/')
def get_all_product():
    pass