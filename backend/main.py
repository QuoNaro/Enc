from datetime import timedelta
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from database.database import engine , Base , SessionLocal
from models.models import User
import services.auth as auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()

# Настройка CORS
origins = [
    "http://localhost:8080",  # Разрешаем запросы с фронтенда на порту 8080
    "http://127.0.0.1:8080",  # Альтернативный адрес для локальной разработки
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Список разрешенных источников
    allow_credentials=True,         # Разрешаем отправку cookies
    allow_methods=["*"],            # Разрешаем все HTTP-методы
    allow_headers=["*"],            # Разрешаем все заголовки
)



# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/signup")
async def signup(user: auth.UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Received data: {user}")
    try:
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        
        hashed_password = auth.get_password_hash(user.password)
        new_user = User(username=user.username, password_hash=hashed_password)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"msg": "User created successfully"}
    except Exception as e:
        logger.error(f"Error during signup: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    

from pydantic import BaseModel
from fastapi import HTTPException, status

# Определите модель данных для входа
class LoginRequest(BaseModel):
    username: str
    password: str

from sqlalchemy.exc import SQLAlchemyError

@app.post("/login")
async def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for username: {form_data.username}")
    try:
        # Получение пользователя из базы данных
        user = db.query(User).filter(User.username == form_data.username).first()
        if not user or not auth.verify_password(form_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Создание токена доступа
        access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth.create_access_token(
            data={"sub": user.username}, 
            expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
    
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")
    
    except Exception as e:
        logger.error(f"Error during login: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    Получает текущего пользователя на основе JWT-токена.
    """
    username = auth.verify_token(token, db)
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user

@app.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Эндпоинт для выхода из аккаунта.
    """
    try:
        # Добавляем токен в черный список (если используется)
        auth.blacklist_token(db, token)

        # Возвращаем успешный ответ
        return {"message": "Successfully logged out"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Logout failed")
    
    