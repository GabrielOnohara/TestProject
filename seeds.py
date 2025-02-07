from sqlalchemy.orm import sessionmaker
from models import User
from db import get_engine

# Function to seed 10 users
def seed_users():
    session = sessionmaker(bind=get_engine())()  # Create a new session
    try:
        # Check if users already exist to prevent duplicates
        if session.query(User).count() == 0:
            # Generate 10 users
            for i in range(1, 11):
                user = User(name=f"User {i}", email=f"user{i}@example.com")
                session.add(user)
            session.commit()  # Commit the changes
            print("10 users seeded successfully.")
        else:
            print("Users already exist in the database.")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error seeding users: {e}")
    finally:
        session.close()

# You can call seed_users when the app starts, or manually if you prefer
# seed_users()
