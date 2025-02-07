# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

# Função para obter o engine
def get_engine():
    return create_engine(DATABASE_URL)

# Criação da sessão
Session = sessionmaker(bind=get_engine())
