from sqlalchemy.orm import declarative_base
from db import get_engine

Base = declarative_base()

def create_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_db()