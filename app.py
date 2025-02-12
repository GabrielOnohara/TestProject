import falcon
from routes import add_routes

from seeds import seed_users, seed_pets
seed_users()
seed_pets()

# app = falcon.asgi.App()
app = falcon.App()
add_routes(app)