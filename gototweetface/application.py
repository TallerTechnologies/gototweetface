__author__ = 'moreno'

from gototweetface.handlers.facebook_handler import FacebookHandler
from gototweetface.handlers.google_handler import GoogleHandler
from gototweetface.handlers.twitter_handler import TwitterHandler
from tornado import web

TWITTER = TwitterHandler
FACEBOOK = FacebookHandler
GOOGLE = GoogleHandler

APPLICATION = web.Application(
    [
        (r'.*/google', GOOGLE),
        (r'.*/facebook', FACEBOOK),
        (r'.*/twitter', TWITTER)
    ])