__author__ = 'moreno'

import os
from gototweetface.handlers.facebook_handler import FacebookHandler
from gototweetface.handlers.google_handler import GoogleHandler
from gototweetface.handlers.twitter_handler import TwitterHandler
from gototweetface.handlers.base_handler import BaseHandler
from tornado import web


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

application = web.Application(
    [   (r'/static',web.StaticFileHandler, {'path': os.path.join(BASE_DIR, "static")}),
        (r'/favicon.ico', web.StaticFileHandler, {'path': os.path.join(BASE_DIR, "static")}),
        (r'.*/google', GoogleHandler),
        (r'.*/facebook', FacebookHandler),
        (r'.*/twitter', TwitterHandler),
        (r'/', BaseHandler)
    ])

application.settings.update({"cookie_secret": "esteEsMiCookieMagico12345"})
