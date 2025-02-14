import falcon
from db import Session
from models import User
from .base import BaseResource

class UserResource(BaseResource):
    def on_get(self, req, resp):
        session = Session()

        page_size, page_number = self.get_pagination_params(req)
        query = self.filter_users(session, req)

        users = query.offset((page_number - 1) * page_size).limit(page_size).all()
        
        resp.media = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
        resp.status = falcon.HTTP_200

        session.close()

    def filter_users(self, session, req):
        name = req.get_param('name')
        email = req.get_param('email')
        query = session.query(User)

        if name:
            query = query.filter(User.name.ilike(f"%{name}%"))

        if email:
            query = query.filter(User.email.ilike(f"%{email}%"))

        return query

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

    def on_delete(self, _req, resp, user_id):
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
