from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import session

from .. import database, schema, model, security, utility


router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(user_Credential: Annotated[OAuth2PasswordRequestForm, Depends()], db: session = Depends(database.get_db)):

    user = db.query(model.Users).filter(
        model.Users.username == user_Credential.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
    if not utility.verify(user_Credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=' invalid credentia')
    # create a token
    # return token

    access_token = security.create_access_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'Bearer'}
