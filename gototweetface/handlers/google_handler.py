from tornado import web, auth, gen

__author__ = 'moreno'


class GoogleHandler(web.RequestHandler, auth.GoogleMixin):

    @web.asynchronous
    @gen.engine
    def get(self):
        if self.get_argument("openid.mode", None):
            user = yield self.get_authenticated_user()
            # self.set_secure_cookie(user.get('claimed_id', None), user)
              # Save the user with e.g. set_secure_cookie()
            self.redirect("/facebook")
        else:
            self.authenticate_redirect()
