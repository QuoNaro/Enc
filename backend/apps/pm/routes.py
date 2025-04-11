from fastapi import APIRouter

from apps.api.v1 import router 






@router.get('/api/get-password-settings')
async def get_settings_for_vue():
    from settings import PasswordSettings
    return PasswordSettings().model_dump()
