import falcon
from db import Session
from models import User

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

    def on_put(self, req, resp, user_id):
        session = Session()
        data = req.media
        user = session.query(User).get(user_id)
        if user:
            user.name = data['name']
            user.email = data['email']
            session.commit()
            resp.media = {'id': user.id, 'name': user.name, 'email': user.email}
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'message': 'User not found'}
        session.close()

    def on_delete(self, req, resp, user_id):
        session = Session()
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            resp.status = falcon.HTTP_204
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'message': 'User not found'}
        session.close()
