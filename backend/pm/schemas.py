from pydantic import BaseModel

# Модель для запроса
class UnlockPasswordRequest(BaseModel):
    password_id: int

# Модель для ответа
class UnlockPasswordResponse(BaseModel):
    password: str
