from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    pets = relationship("Pet", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"