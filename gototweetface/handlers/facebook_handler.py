import tornado
from tornado.template import Template
__author__ = 'moreno'

from tornado import web
from tornado.auth import OpenIdMixin

class FacebookHandler(web.RequestHandler):

    @web.asynchronous
    def get(self):
        template = Template("<html><b> Hola viteh </b></html>")
        self.write("<html><b> Hola viteh </b></html>")
        self.finish()