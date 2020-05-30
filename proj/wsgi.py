import os

from myframe.wsgi import get_wsgi_application

application = get_wsgi_application('proj.settings')
