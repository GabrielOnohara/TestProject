import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

if ENVIRONMENT == 'test':
    DATABASE_URL = "postgresql://myuser:mypassword@db:5432/test_dbname"
else:
    DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

def get_engine():
    return create_engine(DATABASE_URL)

Session = sessionmaker(bind=get_engine())
Base = declarative_base()
