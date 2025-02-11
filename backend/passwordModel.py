from pydantic import Field, BaseModel, ValidationError
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла (если он существует)
load_dotenv()

class PasswordSettings(BaseSettings):
    min_length: int = Field(default=8, ge=1)  # Минимальная длина пароля (стандартное значение: 8)
    max_length: int = Field(default=64, gt=7)  # Максимальная длина пароля (стандартное значение: 64)
    require_uppercase: bool = Field(default=True)  # Требовать заглавные буквы (стандартное значение: True)
    require_lowercase: bool = Field(default=True)  # Требовать строчные буквы (стандартное значение: True)
    require_digit: bool = Field(default=True)  # Требовать цифры (стандартное значение: True)
    require_special_char: bool = Field(default=False)  # Требовать специальные символы (стандартное значение: False)
    allowed_special_chars: str = Field(default="!@#$%^&*()-_=+[]{}|;:,.<>?/~`")  # Допустимые специальные символы (стандартное значение)

    class Config:
        env_prefix = "PASSWORD_"  # Префикс для переменных окружения
        case_sensitive = False  # Игнорировать регистр при поиске переменных


class PasswordValidationErrors(BaseModel):
    """Словарь кодов ошибок и их описаний."""
    length_error: str = "Password length must be between {min} and {max} characters."
    uppercase_error: str = "Password must contain at least one uppercase letter."
    lowercase_error: str = "Password must contain at least one lowercase letter."
    digit_error: str = "Password must contain at least one digit."
    special_char_error: str = "Password must contain at least one special character from: {allowed_chars}."


class Password(BaseModel):
    password: str = Field(..., min_length=1)  # Пароль должен быть строкой
    settings: PasswordSettings = PasswordSettings()  # Настройки пароля
    error_codes: PasswordValidationErrors = PasswordValidationErrors()  # Словарь кодов ошибок

    @staticmethod
    def validate_password(value: str, settings: PasswordSettings, error_codes: PasswordValidationErrors) -> dict:
        errors = {}

        # Проверка длины пароля
        if not (settings.min_length <= len(value) <= settings.max_length):
            errors["PASS-001"] = error_codes.length_error.format(
                min=settings.min_length, max=settings.max_length
            )

        # Проверка наличия заглавных букв
        if settings.require_uppercase and not any(c.isupper() for c in value):
            errors["PASS-002"] = error_codes.uppercase_error

        # Проверка наличия строчных букв
        if settings.require_lowercase and not any(c.islower() for c in value):
            errors["PASS-003"] = error_codes.lowercase_error

        # Проверка наличия цифр
        if settings.require_digit and not any(c.isdigit() for c in value):
            errors["PASS-004"] = error_codes.digit_error

        # Проверка наличия специальных символов
        if settings.require_special_char:
            if not any(c in settings.allowed_special_chars for c in value):
                errors["PASS-005"] = error_codes.special_char_error.format(
                    allowed_chars=settings.allowed_special_chars
                )
        

        return errors

    @property
    def is_valid(self) -> bool:
        """Проверяет, является ли пароль валидным."""
        errors = self.validate_password(self.password, self.settings, self.error_codes)
        return not errors

    @property
    def validation_errors(self) -> dict:
        """Возвращает словарь ошибок валидации."""
        return self.validate_password(self.password, self.settings, self.error_codes)

