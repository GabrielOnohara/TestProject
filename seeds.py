from sqlalchemy.orm import sessionmaker
from models import User
from db import get_engine

def seed_users():
    session = sessionmaker(bind=get_engine())()
    try:
        if session.query(User).count() == 0:
            for i in range(1, 11):
                user = User(name=f"User {i}", email=f"user{i}@example.com")
                session.add(user)
            session.commit()
            print("10 users seeded successfully.")
        else:
            print("Users already exist in the database.")
    except Exception as e:
        session.rollback()
        print(f"Error seeding users: {e}")
    finally:
        session.close()