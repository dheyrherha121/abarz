from fastapi import FastAPI, status,Depends, HTTPException, APIRouter
from .. import schema,utility,model
from sqlalchemy.orm import session
from ..database import get_db


router = APIRouter(
    prefix= '/users',
    tags= ['users']
)
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(user: schema.UserIn, db: session=Depends(get_db)):
    #hash the password from user password
    hash_password = utility.hash(user.password)
    user.password = hash_password
    new_user = model.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', tags= ['users'])
def get_user(id: int, db: session = Depends(get_db)):
    user = db.query(model.Users).filter(model.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user with {id} does not exit')
    return user