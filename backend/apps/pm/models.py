from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, 
    ForeignKey, DateTime, 
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from modules.security.encrypted_json import EncryptedJSON
from db import Base
from modules.security.permissions.types import PermissionTypeEnum # Импорт ENUM

class SecureData(Base):
    __tablename__ = 'secure_data'
    
    data_id = Column(Integer, primary_key=True)
    user_id_owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    service_name = Column(String(100), nullable=False)
    data_type = Column(String(50), nullable=False)
    encrypted_data = Column(EncryptedJSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    owner = relationship('User', back_populates='secure_data')
    permissions = relationship('Permission', back_populates='secure_data')
    group_permissions = relationship('GroupPermission', back_populates='secure_data')
    user_permissions = relationship('UserPermission', back_populates='secure_data')  # Добавлено

class Permission(Base):
    __tablename__ = 'permissions'
    
    permission_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    data_id = Column(Integer, ForeignKey('secure_data.data_id', ondelete='CASCADE'), nullable=False)
    permission_type = Column(PermissionTypeEnum, nullable=False)  # Использование ENUM
    granted_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        UniqueConstraint('user_id', 'data_id'),
    )
    
    # Отношения
    user = relationship('User', foreign_keys=[user_id], back_populates='permissions')
    secure_data = relationship('SecureData', back_populates='permissions')
    granted_by_user = relationship('User', foreign_keys=[granted_by], back_populates='granted_permissions')

class Group(Base):
    __tablename__ = 'groups'
    
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    creator = relationship('User', back_populates='created_groups')
    members = relationship('UserGroup', back_populates='group')
    permissions = relationship('GroupPermission', back_populates='group')

class UserGroup(Base):
    __tablename__ = 'user_groups'
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE'), primary_key=True)
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    user = relationship('User', back_populates='groups')
    group = relationship('Group', back_populates='members')

class GroupPermission(Base):
    __tablename__ = 'group_permissions'
    
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE'), primary_key=True)
    data_id = Column(Integer, ForeignKey('secure_data.data_id', ondelete='CASCADE'), primary_key=True)
    permission_type = Column(PermissionTypeEnum, nullable=False)  # Использование ENUM
    granted_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    group = relationship('Group', back_populates='permissions')
    secure_data = relationship('SecureData', back_populates='group_permissions')
    granted_by_user = relationship('User', back_populates='granted_group_permissions')

class UserPermission(Base):
    __tablename__ = 'user_permissions'
    
    permission_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    data_id = Column(Integer, ForeignKey('secure_data.data_id', ondelete='CASCADE'), nullable=False)
    permission_type = Column(PermissionTypeEnum, nullable=False)
    granted_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        UniqueConstraint('user_id', 'data_id'),
    )
    
    # Отношения
    user = relationship('User', foreign_keys=[user_id])
    secure_data = relationship('SecureData', back_populates='user_permissions')
    granted_by_user = relationship('User', foreign_keys=[granted_by])