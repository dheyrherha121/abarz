from fastapi import  Depends, HTTPException, status, APIRouter
from .. import schema, model, security
from ..database import get_db
from sqlalchemy.orm import session
from .. import security


router = APIRouter(
    prefix='/products',
    tags=['product']
)


@router.get('/')
def get_post(db: session = Depends(get_db)):
    product = db.query(model.Products).filter(model.Products).all()
    return {product}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_poduct(product: schema.Product, db: session = Depends(get_db), current_user: str = Depends(security.get_current_user)):

    # print(current_user.id)
    new_product = model.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    # print(new_post)
    return {new_product}


@router.get('/{id}')  # , response_model= List[schema.Post])
def quary_by_one(id: int, db: session = Depends(get_db),current_user:str =  Depends(security.get_current_user)):
    product = db.query(model.Products).filter(model.Products.id == id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail='the product you are looking for does not exist, check again')
    return {product}


@router.delete('/')
def delete_post(id: int, db: session = Depends(get_db), current_user:str  = Depends(security.get_current_user)):
    delee = db.query(model.Products).filter(model.Products.id == id)
    product = delee.first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='the post with the id is not found')

    delee.delete(synchronize_session=False)
    db.commit()
    return {'product has been deleted '}


@router.put('/{id}')
def updating_post(id: int, product: schema.Product, db: session = Depends(get_db), current_user: int = Depends(security.get_current_user)):
    updte = db.query(model.Products).filter(model.Products.id == id)
    product = updte.first()
    if product == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=' product not found')
    updte.update(product.dict(), synchronize_session=False)
    db.commit()

    return {'successful': updte.first()}
