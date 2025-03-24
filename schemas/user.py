
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    username: str
    email : EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : str = None

