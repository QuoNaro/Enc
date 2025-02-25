from typing import Optional
from settings import ALGORITHM, AppSettings
from datetime import datetime, timedelta, timezone
from jose import jwt

SETTINGS = AppSettings()
SECRET_KEY = SETTINGS.secret_key


def create_access_token(
    data: dict, 
    expires_delta: Optional[timedelta] = None  # Устанавливаем дефолтное значение как None
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
    print(to_encode)
    # Если expires_delta не передан, используем значение из SETTINGS
    if expires_delta is None:
        expires_delta = timedelta(minutes=SETTINGS.jwt_expire_minutes)
    
    # Вычисляем время истечения токена
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    
    # Кодируем данные в JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt