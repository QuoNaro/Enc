from fastapi import APIRouter, Depends

from .password_validator import Password
from .schemas import Token,UserCreate, PasswordRequest
from  db import get_db
from .security import authenticate_user,create_access_token, register_user
from .models import User
from pm.models import Permission
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session



router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # Регистрируем пользователя
    new_user = register_user(user, db)

    # Создаем токен доступа
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/check_username/")
async def check_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    
    if user:
        return {"available": False, "message": "Username already taken"}
    return {"available": True, "message": "Username is available"}

@router.post("/register/admin", response_model=Token)
async def register_admin(user: UserCreate, db: Session = Depends(get_db)):
    # Регистрируем пользователя
    new_user = register_user(user, db)

    # Добавляем права админа этому пользователю     
    for perm in ["edit","read"]:
        new_perm = Permission(entity_type="user", entity_id=new_user.id, permission=perm)
        db.add(new_perm)
    db.commit()
    
    # Создаем токен доступа
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/api/get-password-settings')
async def get_settings_for_vue():
    from settings import PasswordSettings
    return PasswordSettings().model_dump()

@router.post('/api/validate-password')
async def validate_password(password : PasswordRequest):
    password = Password(password=password.password)
    valid = password.is_valid
    errors = password.validation_errors
    result = {'is_valid' : valid, 'errors' : errors }
    return result