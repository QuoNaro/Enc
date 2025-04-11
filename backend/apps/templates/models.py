from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, 
    ForeignKey, DateTime, 
    UniqueConstraint,JSON
)
from sqlalchemy.orm import relationship
from modules.security.encrypted_json import EncryptedJSON
from db import Base
from modules.security.permissions.types import PermissionTypeEnum # Импорт ENUM

class Templates(Base):
    __tablename__ = 'templates'
    id = Column(Integer,primary_key=True,index=True)
    template = Column(JSON)