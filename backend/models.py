from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)


# Database setup
engine = create_engine('postgresql://encrypuser:182801xarf@0.0.0.0:5432/encryption')
Base.metadata.create_all(engine)


# Session setup
Session = sessionmaker(bind=engine)
session = Session()
