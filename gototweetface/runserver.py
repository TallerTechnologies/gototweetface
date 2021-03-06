__author__ = 'moreno'

import sys

from tornado import ioloop
from gototweetface.application import application


if __name__ == '__main__':
    PORT = 8000
    if len(sys.argv)==2:
        PORT = int(sys.argv[1].lstrip('--port='))
    application.listen(PORT)
    print "Running on port {}".format(PORT)
    ioloop.IOLoop.instance().start()
