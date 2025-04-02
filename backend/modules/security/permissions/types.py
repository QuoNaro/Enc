from enum import Enum
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM

class PermissionType(Enum):
    READ = 'read'
    WRITE = 'write'
    ADMIN = 'admin'

# SQLAlchemy ENUM для использования в моделях
PermissionTypeEnum = PG_ENUM(
    PermissionType,
    name='permission_type',
    create_type=True  # Создаст ENUM в БД при миграции
)