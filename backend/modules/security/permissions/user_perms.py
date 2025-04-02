from sqlalchemy.orm import Session
from models.user import User
from models.secure_data import SecureData
from .types import PermissionType
from apps.pm.models import UserPermission

def grant_permission(
    target_user: User,
    data: SecureData,
    permission_type: PermissionType,
    granted_by: User,
    db: Session = get_db(),
    ):
    if not granted_by.is_admin:
        raise PermissionError("Only admins can grant permissions")
        
    existing = db.query(UserPermission).filter(
        UserPermission.user_id == target_user.id,
        UserPermission.data_id == data.data_id
    ).first()
    
    if existing:
        existing.permission_type = permission_type.value
    else:
        perm = UserPermission(
            user_id=target_user.id,
            data_id=data.data_id,
            permission_type=permission_type.value,
            granted_by=granted_by.id
        )
        db.add(perm)
    db.commit()
      
def revoke_permission(
    target_user: User,
    data: SecureData,
    db: Session = get_db(),
    ):
    db.query(UserPermission).filter(
        UserPermission.user_id == target_user.id,
        UserPermission.data_id == data.data_id
    ).delete()
    db.commit()

def has_permission(
    user: User,
    data: SecureData,
    required_permission: PermissionType,
    db: Session = get_db(),
    ) -> bool:
    perm = db.query(UserPermission).filter(
        UserPermission.user_id == user.id,
        UserPermission.data_id == data.data_id,
        UserPermission.permission_type == required_permission.value
    ).first()
    return perm is not None