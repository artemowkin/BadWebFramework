import os

ROOT_URLCONF = 'proj.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = 'templates'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
