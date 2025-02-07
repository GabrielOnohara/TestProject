from seeds import seed_users, seed_pets
seed_users()
seed_pets()

import falcon
import json
from sqlalchemy.orm import scoped_session, joinedload

from db import Session
from models import User, Pet


class RootResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Welcome to Falcon API'}

class UserResource:
    def on_get(self, req, resp):
        session = Session()
        users = session.query(User).all()
        resp.media = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
        session.close()

    def on_post(self, req, resp):
        session = Session()
        data = req.media
        new_user = User(name=data['name'], email=data['email'])
        session.add(new_user)
        session.commit()
        resp.status = falcon.HTTP_201
        resp.media = {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}
        session.close()

class PetResource:
    def on_get(self, req, resp):
        session = Session()
        pets = session.query(Pet).all()
        resp.media = [{'id': pet.id, 'name': pet.name, 'species': pet.species} for pet in pets]
        session.close()

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


# app = falcon.asgi.App()
app = falcon.App()

app.add_route('/', RootResource())
app.add_route('/users', UserResource())
app.add_route('/pets', PetResource())
app.add_route('/user_pets', UserPetsResource())
