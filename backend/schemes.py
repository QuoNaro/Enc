from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    emails: List[EmailStr] = []
    passwords: List['Password'] = []

    class Config:
        orm_mode = True

class EmailBase(BaseModel):
    email: EmailStr

class EmailCreate(EmailBase):
    pass

class Email(EmailBase):
    id: int
    user_id: int
    user: Optional[User] = None

    class Config:
        orm_mode = True

class PasswordBase(BaseModel):
    service: str
    username: str
    password: str

class PasswordCreate(PasswordBase):
    pass

class Password(PasswordBase):
    id: int
    user_id: int
    user: Optional[User] = None

    class Config:
        orm_mode = True

User.update_forward_refs()
