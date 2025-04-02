
from models.group import Group
from modules.security.user_auth import get_db
from models.secure_data import SecureData
from .types import PermissionType
from apps.pm.models import GroupPermission

def grant_group_permission(
    group: Group,
    data: SecureData,
    permission_type: PermissionType,
    granted_by: User,
    db: Session = get_db(),
    ):
    if not granted_by.is_admin:
        raise PermissionError("Only admins can grant group permissions")
        
    existing = db.query(GroupPermission).filter(
        GroupPermission.group_id == group.group_id,
        GroupPermission.data_id == data.data_id
    ).first()
    
    if existing:
        existing.permission_type = permission_type.value
    else:
        perm = GroupPermission(
            group_id=group.group_id,
            data_id=data.data_id,
            permission_type=permission_type.value,
            granted_by=granted_by.id
        )
        db.add(perm)
    db.commit()

def revoke_group_permission(
    group: Group,
    data: SecureData,
    db: Session = get_db(),
    ):
    db.query(GroupPermission).filter(
        GroupPermission.group_id == group.group_id,
        GroupPermission.data_id == data.data_id
    ).delete()
    db.commit()

def group_has_permission(
    group: Group,
    data: SecureData,
    required_permission: PermissionType,
    db: Session = get_db(),
    ) -> bool:
    perm = db.query(GroupPermission).filter(
        GroupPermission.group_id == group.group_id,
        GroupPermission.data_id == data.data_id,
        GroupPermission.permission_type == required_permission.value
    ).first()
    return perm is not None