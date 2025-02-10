from db import Session
from models import Pet

class PetResource:
    def on_get(self, req, resp):
        session = Session()
        pets = session.query(Pet).all()
        resp.media = [{'id': pet.id, 'name': pet.name, 'species': pet.species} for pet in pets]
        session.close()