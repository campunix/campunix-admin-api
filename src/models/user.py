from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.v1 import validator


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


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError("New password and confirm password do not match")
        return v

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str