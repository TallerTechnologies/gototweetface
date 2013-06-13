from tornado import web, auth, gen
from tornado.gen import coroutine

__author__ = 'moreno'


class GoogleHandler(web.RequestHandler, auth.GoogleMixin):

    @web.asynchronous
    @coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            user = yield self.get_authenticated_user()
            # self.set_secure_cookie(user.get('claimed_id', None), )
              # Save the user with e.g. set_secure_cookie()

            message = "Hello " + user['name']
            message_mail = "Your e-mail is " + user['email']
            template = "<html> " + \
                        "<head><title>Google</title></head>" + \
                        "<body>" + \
                        "<b>" + message + "</b> <br>" + \
                        message_mail + \
                       "</html>"
            self.write(template)
            self.finish()
        else:
            self.authenticate_redirect()
