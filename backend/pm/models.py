from sqlalchemy import Column, ForeignKey, Integer, String
from auth.models import User
from db import Base, get_db

class Password(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    

# Модель Group
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Модель Permission
class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String, nullable=False)  # 'user' или 'group'
    entity_id = Column(Integer, nullable=False)   # ID связанной сущности
    permission = Column(String, nullable=False)   # Разрешение (строка или JSON)

    # Полиморфная связь
    @property
    def entity(self):
        session = get_db()
        if self.entity_type == "user":
            return session.query(User).get(self.entity_id)
        elif self.entity_type == "group":
            return session.query(Group).get(self.entity_id)
        return None