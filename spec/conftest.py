import pytest
from falcon.testing import TestClient
from db import Session
from models import User, Pet
from app import app

@pytest.fixture
def client_fixture():
    """Fixture para o cliente de teste"""
    return TestClient(app)

@pytest.fixture
def db_user_pets_setup():
    """Fixture para configurar o banco de dados com usuários e pets para os testes"""
    session = Session()
    session.query(Pet).delete()
    session.query(User).delete()
    session.commit()
    session.close()

    # Criação de um usuário e seu pet
    user = User(name="John Doe", email="john.doe@example.com")
    pet = Pet(name="Buddy", species="Dog")
    user.pets.append(pet)
    session.add(user)
    session.add(pet)
    session.commit()
    user_id = user.id

    session.close()
    return user_id