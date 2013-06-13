__author__ = 'moreno'

from gototweetface.handlers.facebook_handler import FacebookHandler
from gototweetface.handlers.google_handler import GoogleHandler
from gototweetface.handlers.twitter_handler import TwitterHandler
from gototweetface.handlers.base_handler import BaseHandler
from tornado import web

application = web.Application(
    [
        (r'.*/google', GoogleHandler),
        (r'.*/facebook', FacebookHandler),
        (r'.*/twitter', TwitterHandler),
        (r'.*/(\w+?)/hello', BaseHandler)
    ])

application.settings["cookie_secret"] = "esteEsMiCookieMagico12345"