import os
import importlib

from myframe.settings import Settings
from myframe.http import HTTPRequest, HTTPResponse


class WSGIHandler:

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.request = HTTPRequest(environ)

    def __iter__(self):
        response = self.start_response()
        self.start(response.status, response.headers)
        yield response.response_text

    def start_response(self):
        if not self.request.path.endswith('/'):
            return HTTPResponse(status_code=301, headers=[
                ('Location', f'{self.request.path}/')
            ])

        settings = Settings()
        main_urlconf = settings['ROOT_URLCONF']
        main_urlconf_module = importlib.import_module(main_urlconf)
        if not hasattr(main_urlconf_module, 'urlpatterns'):
            raise ValueError(f"{main_urlconf} needs to have `urlpatterns`")

        return self.parse_urlpatterns(main_urlconf_module.urlpatterns)

    def parse_urlpatterns(self, urlpatterns):
        if not isinstance(urlpatterns, dict):
            raise ValueError('`urlpatterns` need to be dict')

        for pattern, view in urlpatterns.items():
            if pattern in self.request.path:
                if isinstance(view, dict):
                    return self.parse_urlpatterns(view)
                else:
                    return view(self.request)

        return HTTPResponse(status_code=404)


def get_wsgi_application(settings_module):
    os.environ.setdefault('MYFRAME_SETTINGS_MODULE', settings_module)
    return WSGIHandler
