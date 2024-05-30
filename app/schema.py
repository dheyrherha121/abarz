from pydantic import BaseModel, EmailStr
import datetime
from typing import Optional

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_now: datetime.datetime

    class config:
        from_attribute = True

class Product(BaseModel):
    title: str
    desciption: str
    price: int
class Token(BaseModel):
    acces_token: str
    token_type: str
class TokenData(BaseModel):
    id: Optional[int] = None  