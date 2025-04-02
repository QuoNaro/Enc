from modules.security.user_auth import get_current_user
from fastapi import Request
from apps.auth.schemas import User
from main import create_app

app = create_app()

class CRequest(Request):
    user_data: User  # Добавляем атрибут для данных пользователя

@app.middleware("http")
async def add_user_data_to_request(request: CRequest, call_next):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user = None
    is_authenticated = False

    if token:
        user = get_current_user(token)
        is_authenticated = user is not None

    # Устанавливаем данные в кастомный Request
    request.state.user_data = User(
        user=user,
        is_authenticated=is_authenticated
    )
    
    response = await call_next(request)
    return response

