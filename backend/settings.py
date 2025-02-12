from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional

# Определение базовой директории
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

class EncSettings(BaseSettings):
    class Config:
        extra = 'allow'
        env_file = ENV_PATH
        case_sensitive = False

class PasswordSettings(EncSettings):
    min_length: int = Field(default=8, ge=1)  # Минимальная длина пароля
    max_length: int = Field(default=64, gt=7)  # Максимальная длина пароля
    require_uppercase: bool = Field(default=True)  # Требовать заглавные буквы
    require_lowercase: bool = Field(default=True)  # Требовать строчные буквы
    require_digit: bool = Field(default=True)  # Требовать цифры
    require_special_char: bool = Field(default=False)  # Требовать специальные символы
    allowed_special_chars: str = Field(default="!@#$%^&*()-_=+[]{}|;:,.<>?/~`")  # Допустимые специальные символы

    class Config:
        env_prefix = "PASSWORD_"

class DatabaseSettings(EncSettings):
    host: Optional[str] = None
    db: Optional[str] = None
    password: Optional[str] = None
    port: Optional[int] = None
    user: Optional[str] = None

    class Config:
        env_prefix = "DATABASE_"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

class AppSettings(EncSettings):
    secret_key: str
    jwt_expire_minutes: int
    
    class Config:
        env_prefix = "APP_"
