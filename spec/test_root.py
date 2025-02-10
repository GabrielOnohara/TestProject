import pytest
import falcon
from falcon.testing import TestClient

from db import Session
from models import User, Pet
from app import app

@pytest.fixture
def client():
    return TestClient(app)
    
def test_root(client):
    response = client.simulate_get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to Falcon API'}
