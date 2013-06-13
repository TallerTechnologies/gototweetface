import tornado
__author__ = 'moreno'

from tornado import web
from tornado.auth import OpenIdMixin

class FacebookHandler(web.RequestHandler):

    @web.asynchronous
    def get(self):
        template = "<html><b> Hola viteh </b></html>"
        self.write(template)
        self.finish()