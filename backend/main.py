from fastapi import FastAPI
from database import engine , Base , SessionLocal
from models import  User

import auth
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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

from fastapi import Depends
from sqlalchemy.orm import Session

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import HTTPException

import logging

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