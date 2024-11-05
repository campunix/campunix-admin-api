from typing import Optional
from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    disabled: Optional[bool] = False

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    confirm_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserPublic(BaseModel):
    id: int
    username: str
    full_name: str


