from fastapi import APIRouter,Depends, Request
from db import get_db
from sqlalchemy.orm import Session
from apps.templates.models import Templates
from apps.api.v1 import router




@router.post('/new-template')
async def save_template(request : Request, ):
    if request.state.user.is_authenticated :
        ...
    return {}

@router.get('/get-templates')
async def get_templates(request : Request):
    return request.state.db.query(Templates).all()
    
