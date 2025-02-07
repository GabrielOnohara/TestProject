from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

def get_engine():
    return create_engine(DATABASE_URL)

Session = sessionmaker(bind=get_engine())
