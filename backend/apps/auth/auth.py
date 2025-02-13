from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from apps.auth.schemas import TokenData
from apps.auth.database import get_db
from settings import ALGORITHM, OAUTH2_SCHEME, AppSettings, PWD_CONTEXT
from apps.auth.models import User

SETTINGS = AppSettings()
SECRET_KEY = SETTINGS.secret_key

def get_current_user(db: Session = Depends(get_db), token: str = Depends(OAUTH2_SCHEME)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось проверить учетные данные",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def verify_password(plain_password, hashed_password):
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(password):
    return PWD_CONTEXT.hash(password)

def create_access_token(data : dict, expires_delta: Optional[timedelta]= None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
        
def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)  # **Исправлено: убран параметр password**
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
