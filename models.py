# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db import get_engine  # Importando a função get_engine

Base = declarative_base()

# Definindo o modelo
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Usando a função get_engine() para criar o engine
engine = get_engine()

# Criando as tabelas
Base.metadata.create_all(engine)
