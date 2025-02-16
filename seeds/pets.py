from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from models import Pet, User
from db import get_engine

def seed_pets():
    session = sessionmaker(bind=get_engine())()
    try:
        # Check if pets already exist (to avoid seeding duplicate pets)
        if session.query(Pet).count() <= 1:
            # Get all the users in the database
            users = session.query(User).all()
            if not users:
                print("No users found in the database. Please seed users first.")
                return

            for user in users:
                # Create three pets for each user
                dog = Pet(name=f"Dog {user.id}", species="dog", user_id=user.id)
                cat = Pet(name=f"Cat {user.id}", species="cat", user_id=user.id)
                fish = Pet(name=f"Fish {user.id}", species="fish", user_id=user.id)
                session.add_all([dog, cat, fish])

            session.commit()
            print("Pets seeded successfully.")
        else:
            print("Pets already exist in the database.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error seeding pets: {e}")
    finally:
        session.close()
