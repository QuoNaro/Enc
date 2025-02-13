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


def verify_password(
    plain_password: str, 
    hashed_password: str
) -> bool:
    """
    Проверяет соответствие открытого пароля его хэшу.

    Parameters:
        plain_password (str): Открытый пароль.
        hashed_password (str): Хэшированный пароль.

    Returns:
        bool: True если пароли совпадают, иначе False.
    """
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(
    password: str
) -> str:
    """
    Создает хэш для заданного пароля.

    Parameters:
        password (str): Пароль для хэширования.

    Returns:
        str: Хэшированный пароль.
    """
    return PWD_CONTEXT.hash(password)


def create_access_token(
    data: dict, 
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Создает access token с указанными данными.

    Parameters:
        data (dict): Данные для включения в токен.
        expires_delta (Optional[timedelta]): Время жизни токена.

    Returns:
        str: Access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def refresh_access_token(
    refresh_token: str
) -> dict:
    """
    Обновляет access token по refresh token.

    Parameters:
        refresh_token (str): Refresh token.

    Returns:
        dict: Новый access token и тип токена.

    Raises:
        HTTPException: Если refresh token недействителен.
    """
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        
        # Создаем новый access_token
        new_access_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=SETTINGS.jwt_expire_minutes))
        return {"access_token": new_access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


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


def authenticate_user(
    db: "Session", 
    username: str, 
    password: str
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


# Указываем публичный интерфейс
__all__ = ["get_current_user", "authenticate_user"]