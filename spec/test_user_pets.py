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
    user_id = user.id

    session.close()
    return user_id


def test_get_user_pets(client, setup_db):
    user_id = setup_db
    response = client.simulate_get(f'/users/{user_id}/pets')
    assert response.status_code == 200
    user_pets = response.json
    assert user_pets[0]['name'] == "Buddy"
    assert user_pets[0]['species'] == "Dog"

def test_post_user_pets(client, setup_db):
    user_id = setup_db
    new_pet_data = {'name': 'Garfield', 'species': 'Fat Cat'}
    response = client.simulate_post(f'/users/{user_id}/pets', json=new_pet_data)
    assert response.status_code == 201
    user_pets = response.json
    assert user_pets['name'] == "Garfield"
    assert user_pets['species'] == "Fat Cat"