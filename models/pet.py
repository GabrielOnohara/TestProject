from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String, index=True)
    age = Column(Integer, index=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="pets")

    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name}, species={self.species})>"

    def __str__(self):
        return f"Pet: {self.name}, species: {self.species}"