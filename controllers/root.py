class RootResource:
    def on_get(self, resp):
        resp.media = {'message': 'Welcome to Falcon API'}