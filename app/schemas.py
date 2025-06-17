from pydantic import BaseModel, EmailStr

from typing import Optional  

class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BlogBase):
    pass

class BlogOut(BlogBase):
    id:int
    user_id : int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password : str

class UserOut(UserBase):
    id:int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

