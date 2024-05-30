from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Annotated
from . import schema,database, model
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from .config import setting

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = setting.secret_key
ACCESS_MINUTES = setting.access_expires
ALGORITHM = setting.algorithm


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow()  + timedelta(minutes=ACCESS_MINUTES)
    to_encode.update({'exp': expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def VerifyaccessToken(token: str, credential_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
           raise credential_exception
        token_data = schema.TokenData(id = id) 
    except JWTError:
        raise credential_exception
    
    return token_data

def get_current_user(token: Annotated[str, Depends(oauth2_schema)],db: session =  Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='coud not validate credentils', headers={'WWW.Authenticate': 'Bearer'})
    token = VerifyaccessToken(token, credential_exception)
    user = db.query(model.User).filter(model.User.id == token.id).first()
    return user

