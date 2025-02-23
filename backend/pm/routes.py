from fastapi import APIRouter, Depends

from auth.models import User
from  pm.schemas import UnlockPasswordRequest, UnlockPasswordResponse
from db import get_db
from auth.security.user_auth import get_current_user

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter()




@router.post('/api/get-pwd', response_model=UnlockPasswordResponse)
async def unlock_password(
    request: UnlockPasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Эндпоинт для получения защищённого пароля по его ID.
    Пользователь должен быть авторизован.
    """
    # Получаем ID пароля из запроса
    password_id = request.password_id

    if not password_id:
        raise HTTPException(status_code=400, detail="Password ID is required")

    # Ищем пароль в базе данных
    password = db.query(PasswordModel).filter(PasswordModel.id == password_id).first()

    if not password:
        raise HTTPException(status_code=404, detail="Password not found")

    # Проверяем права доступа
    if password.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You do not have permission to access this password")

    # Возвращаем пароль
    return {"password": password.value}