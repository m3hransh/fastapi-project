from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  # Store hashed password, not plain text!
    bio = Column(String(500))
