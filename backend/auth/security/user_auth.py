
from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from auth.schemas import TokenData, UserCreate
from db import get_db
from auth.models import User
from settings import ALGORITHM, OAUTH2_SCHEME, AppSettings
from .password import get_password_hash, verify_password

SETTINGS = AppSettings()
SECRET_KEY = SETTINGS.secret_key


def get_current_user(
    db: "Session" = Depends(get_db), 
    token: str = Depends(OAUTH2_SCHEME)
) -> "User":
    """
    Проверяет токен и возвращает текущего пользователя.

    Parameters:
        db (Session): Сессия базы данных.
        token (str): Токен аутентификации.

    Returns:
        User: Экземпляр модели пользователя.

    Raises:
        HTTPException: Если токен недействителен или пользователь не найден.
    """
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


def get_user(
    db: "Session", 
    username: str
) -> Optional["User"]:
    """
    Ищет пользователя по имени в базе данных.

    Parameters:
        db (Session): Сессия базы данных.
        username (str): Имя пользователя.

    Returns:
        User: Экземпляр модели пользователя или None, если пользователь не найден.
    """
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: "Session", username: str, password: str
) -> Optional["User"]:
    """
    Аутентифицирует пользователя.

    Parameters:
        db (Session): Сессия базы данных.
        username (str): Имя пользователя.
        password (str): Пароль.

    Returns:
        User: Экземпляр модели пользователя, если аутентификация успешна, иначе None.
    """
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def register_user(user_data: UserCreate, db: Session) -> Optional[None | User]:
    
    # Проверяем, существует ли пользователь с таким именем
    db_user = get_user(db, user_data.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Хэшируем пароль и создаем нового пользователя
    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user