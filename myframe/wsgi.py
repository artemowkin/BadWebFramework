import os
import re
import importlib

from myframe.settings import settings
from myframe.http import HTTPRequest, HTTPResponse, HTTPTemplateResponse


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
        if not self.request.path.endswith('/') and self.request.path:
            return HTTPResponse(status_code=307, headers=[
                ('Location', f"/{self.request.path}/")
            ])

        main_urlconf = settings.ROOT_URLCONF
        main_urlconf_module = importlib.import_module(main_urlconf)
        if not hasattr(main_urlconf_module, 'urlpatterns'):
            raise ValueError(f"{main_urlconf} needs to have `urlpatterns`")

        return self.parse_urlpatterns(main_urlconf_module.urlpatterns,
                                      self.request.path)

    def parse_urlpatterns(self, urlpatterns, path):
        if not isinstance(urlpatterns, dict):
            raise ValueError('`urlpatterns` need to be dict')

        if not urlpatterns:
            return HTTPTemplateResponse(template_name='myframe_home.html')

        for pattern, view in urlpatterns.items():
            match = re.match(pattern, path)
            if match:
                if isinstance(view, dict):
                    return self.parse_urlpatterns(view, path[match.end():])
                elif path and not pattern:
                    continue
                else:
                    kwargs = match.groupdict()
                    if kwargs:
                        return view(self.request, **kwargs)

                return view(self.request)

        return HTTPResponse(status_code=404)


def get_wsgi_application():
    return WSGIHandler
