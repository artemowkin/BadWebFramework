import sys
import os

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
))

from myframe.wsgi import get_wsgi_application

application = get_wsgi_application('proj.settings')
