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

def test_get_users(client, setup_db):
    response = client.simulate_get('/users')
    assert response.status_code == 200
    users = response.json
    assert len(users) == 1  # Espera que exista um usuário
    assert users[0]['name'] == "John Doe"
    assert users[0]['email'] == "john.doe@example.com"


def test_post_user(client, setup_db):
    new_user_data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    response = client.simulate_post('/users', json=new_user_data)
    assert response.status_code == 201
    new_user = response.json
    assert new_user['name'] == 'Jane Doe'
    assert new_user['email'] == 'jane.doe@example.com'