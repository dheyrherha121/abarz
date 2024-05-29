from fastapi import APIRouter, status, HTTPException, Depends
from .. import database, model
from sqlalchemy.orm import session
router = APIRouter(
    prefix= 'Products/',
    tags= ['Product']
)

@router('/{id}')
def get_all_product(id: int, db:session = Depends(database.get_db) ):
    product = db.query(model.Products).filter(model.Products.id == id).first()
    return product