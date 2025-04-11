from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request,Depends
from apps.auth.schemas import UserRequest
from jose import jwt
from sqlalchemy.orm import Session
from modules.security.user_auth import get_current_user
from fastapi import HTTPException
from settings import AppSettings
from settings import ALGORITHM
from modules.security.token import decode_token
from db import get_db
from apps.auth.models import User

SECRET_KEY = AppSettings().secret_key


from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from sqlalchemy.orm import Session
from modules.security.token import decode_token
from db import get_db  # Ensure this is your function to get a DB session
from apps.auth.models import User
from settings import AppSettings, ALGORITHM

SECRET_KEY = AppSettings().secret_key



class AddUserDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        is_authenticated = False
        token = None

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.replace("Bearer ", "")

        if token:
            user_data = decode_token(token, SECRET_KEY, ALGORITHM)
            with next(get_db()) as db:  # Ensure the session is properly closed
                request.state.db = db
                user = db.query(User).filter(User.username == user_data['id']).first()
            if user:
                is_authenticated = True
        else: 
            user = User(username='None',hashed_password = None,is_active = False, id = 0)
                
                    
        user_data = UserRequest(**user.__dict__, is_authenticated=is_authenticated)
        
         
        request.state.user = user_data
        
        response = await call_next(request)
        return response