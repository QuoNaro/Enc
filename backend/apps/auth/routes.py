from fastapi import APIRouter, Depends

from apps.auth.schemas import Token,UserCreate, UserResponse
from apps.auth.database import get_db
from apps.auth.password_model import Password
from apps.auth.auth import authenticate_user, create_access_token, get_user,get_password_hash,get_current_user
from apps.auth.models import User

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session





router = APIRouter()


@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Проверяем валидность пароля
    password = Password(password=user.password)
    if not password.is_valid:
        raise HTTPException(status_code=422, detail=password.validation_errors)
    
    # Проверяем, существует ли пользователь с таким именем
    db_user = get_user(db, user.username)  # Убран параметр password
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Хэшируем пароль и создаем нового пользователя
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Создаем токен доступа
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/my', response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
    