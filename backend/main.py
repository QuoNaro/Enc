from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.auth.routes import router as auth_routes
from apps.pm.routes import router as pm_routes
from contextlib import asynccontextmanager
from db import Base,engine


class FolderError(Exception):
    """
    Custom exception class for folder-related errors.
    """
    pass



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    
    # Таблицы созданы
    yield
    
    
app = FastAPI(lifespan=lifespan)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Content-Type", "Authorization"],
# )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Подключение маршрутов
app.include_router(auth_routes)
app.include_router(pm_routes)








        
