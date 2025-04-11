# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db import Base, engine
from typing import Optional
from middleware import AddUserDataMiddleware

# Singleton-переменная для хранения экземпляра приложения
_app: Optional[FastAPI] = None

def create_app() -> FastAPI:
    global _app
    if _app is not None:
        return _app

    # Создаем новый экземпляр приложения
    _app = FastAPI()

    # Middleware
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Lifespan
    @_app.on_event("startup")
    async def startup():
        Base.metadata.create_all(engine)

    # Регистрация роутов
    from apps.auth.routes import router as auth_routes
    from apps.pm.routes import router as pm_routes
    from apps.templates.routes import router as template_routes
    from apps.api.v1 import router as api_routes

    _app.include_router(auth_routes)
    _app.include_router(pm_routes)
    _app.include_router(template_routes)
    _app.include_router(api_routes)
    
    # Регистрация middleware     
    _app.add_middleware(AddUserDataMiddleware)

    return _app

# Создаем основной экземпляр приложения
app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)