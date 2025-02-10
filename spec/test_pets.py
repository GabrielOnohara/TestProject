import pytest
import falcon
from falcon.testing import TestClient

from db import Session
from models import User, Pet
from app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def setup_db():
    session = Session()
    session.query(Pet).delete()
    session.query(User).delete()
    session.commit()
    session.close()

    user = User(name="John Doe", email="john.doe@example.com")
    pet = Pet(name="Buddy", species="Dog")
    user.pets.append(pet)

    session.add(user)
    session.add(pet)
    session.commit()
    session.close()

def test_get_pets(client, setup_db):
    response = client.simulate_get('/pets')
    assert response.status_code == 200
    pets = response.json
    assert len(pets) == 1
    assert pets[0]['name'] == "Buddy"
    assert pets[0]['species'] == "Dog"