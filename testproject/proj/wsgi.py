import sys
import os

from .settings import BASE_DIR

os.environ.setdefault('MYFRAME_SETTINGS_MODULE', 'proj.settings')

sys.path.append(os.path.dirname(BASE_DIR))

from myframe.wsgi import get_wsgi_application

application = get_wsgi_application()
