import falcon
from sqlalchemy.orm import scoped_session
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

# app = falcon.asgi.App()
app = falcon.App()
app.add_route('/users', UserResource())
