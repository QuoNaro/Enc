from sqlalchemy import Column, Integer, String, Boolean
from db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    # Отношения
    secure_data = relationship('SecureData', back_populates='owner')
    permissions = relationship('Permission', foreign_keys="Permission.user_id", back_populates='user')
    granted_permissions = relationship('Permission', foreign_keys="Permission.granted_by", back_populates='granted_by_user')
    granted_group_permissions = relationship('GroupPermission', foreign_keys="GroupPermission.granted_by", back_populates='granted_by_user')
    created_groups = relationship('Group', back_populates='creator')
    groups = relationship('UserGroup', back_populates='user')