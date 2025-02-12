from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.auth.routes import router as auth_routes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Подключение маршрутов
app.include_router(auth_routes)




        
