from tornado import web, auth

__author__ = 'moreno'


class GoogleHandler(web.RequestHandler, auth.GoogleMixin):

    @web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
           self.get_authenticated_user(self.async_callback(self._on_auth))
           return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise web.HTTPError(500, "Google auth failed")
        # Save the user with, e.g., set_secure_cookie()