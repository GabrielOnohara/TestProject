from app import app
from controllers import *

app.add_route('/', RootResource())
app.add_route('/users', UserResource())
app.add_route('/pets', PetResource())
app.add_route('/user_pets', UserPetsResource())