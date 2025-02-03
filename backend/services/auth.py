from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr
from fastapi import Depends, HTTPException, status

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserBase(BaseModel):
    username: str



class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    password_hash: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str = None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(db: Session, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(db: Session, username: str, password: str):
    """
    Аутентифицирует пользователя по логину и паролю.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user






def verify_token(token: str, db: Session):
    """
    Проверяет валидность JWT-токена.
    """
    try:
        # Декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Проверяем срок действия токена
        expiration_time = datetime.fromtimestamp(payload.get("exp"))
        if datetime.utcnow() > expiration_time:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )

        # Проверяем, находится ли токен в черном списке
        if is_token_blacklisted(db, token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been revoked",
            )

        # Возвращаем данные пользователя из токена
        return payload.get("sub")  # Например, username или user_id

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

def blacklist_token(db: Session, token: str):
    """
    Добавляет токен в черный список.
    """
    blacklisted_token = BlacklistedToken(id=token)
    db.add(blacklisted_token)
    db.commit()
    
    
def is_token_blacklisted(db: Session, token: str) -> bool:
    """
    Проверяет, находится ли токен в черном списке.
    """
    blacklisted_token = db.query(BlacklistedToken).filter(BlacklistedToken.id == token).first()
    return blacklisted_token is not None