from seeds import seed_users, seed_pets
seed_users()
seed_pets()

import falcon
# app = falcon.asgi.App()
app = falcon.App()

import routes
