class RootResource:
    def on_get(self, _req, resp):
        resp.media = {'message': 'Welcome to Falcon API'}