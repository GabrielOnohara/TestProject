from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    pets = relationship("Pet", back_populates="owner")