class RootResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Welcome to Falcon API'}