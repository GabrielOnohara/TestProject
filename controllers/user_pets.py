from db import Session
from models import User, Pet
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound

class UserPetsResource:
    def on_get(self, req, resp, user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).options(joinedload(User.pets)).one()
            pets = [{'name': pet.name, 'species': pet.species} for pet in user.pets]
            resp.media = pets
        except NoResultFound:
            resp.status = 404
            resp.media = {'error': 'User not found'}

        session.close()