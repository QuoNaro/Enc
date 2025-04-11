from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserInDB(UserCreate):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    
# Pydantic модель для ответа с данными пользователя
class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool
    class Config:
        from_attributes = True 
        

class PasswordRequest(BaseModel):
    password: str
    
    
class UserRequest(UserResponse):
    is_authenticated: bool
    