from db import Session
from models import User, Pet
from sqlalchemy.orm import joinedload

class UserPetsResource:
    def on_get(self, req, resp):
        session = Session()
        users = session.query(User).options(joinedload(User.pets)).all()
        users_resp = []
        for user in users:
            user_obj = {'id': user.id, 'name': user.name, 'email': user.email, 'pets': []}
            for pet in user.pets:
                user_obj['pets'].append({
                    'name': pet.name,
                    'species': pet.species
                })
            users_resp.append(user_obj)
        print(users_resp)
        resp.media = users_resp
        session.close()