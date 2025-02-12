from controllers import RootResource, UserResource, PetResource, UserPetsResource

def add_routes(app):
    app.add_route('/', RootResource())
    app.add_route('/users', UserResource())
    app.add_route('/users/{user_id}', UserResource())
    app.add_route('/pets', PetResource())
    app.add_route('/user_pets', UserPetsResource())
    app.add_route('/users/{user_id}/pets', UserPetsResource())