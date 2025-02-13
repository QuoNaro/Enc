from typing import Optional
from settings import ALGORITHM, AppSettings
from datetime import datetime, timedelta, timezone
from jose import jwt

SETTINGS = AppSettings()
SECRET_KEY = SETTINGS.secret_key

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
