import os
import mimetypes
from string import Template

from myframe.settings import settings


def status_from_code(status_code):
    if status_code == 200:
        return '200 OK'
    elif status_code == 404:
        return '404 Not Found'
    elif status_code == 405:
        return '405 Method Not Allowed'
    elif status_code == 301:
        return '301 Moved Permanently'
    elif status_code == 307:
        return '307 Temporary Redirect'
    elif status_code == 308:
        return '308 Permanent Redirect'


class HTTPRequest:

    def __init__(self, environ):
        self.path = environ.get('PATH_INFO')
        self.method = environ.get('REQUEST_METHOD')
        self.cookies = environ.get('HTTP_COOKIE', '')

    @property
    def is_static(self):
        if mimetypes.guess_type(self.path)[0]:
            return True

        return False


class HTTPResponse:

    def __init__(self, text='', status_code=200, headers=[]):
        if status_code != 200 and text:
            raise ValueError(
                f'You cannot setup text to {status_code} status code'
            )

        self.status_code = status_code
        self.status = status_from_code(status_code)
        self.response_text = (text.encode() or
                              self.get_response_text(status_code))
        self.headers = headers or self.get_default_headers(status_code)

    def get_response_text(self, status_code):
        if status_code == 404:
            return '<h1>404 Not Found</h1>'.encode()
        elif status_code == 405:
            return '<h1>405 Method Not Allowerd</h1>'.encode()

        return ''.encode()

    def get_default_headers(self, status_code):
        return [('Content-type', 'text/html')]


class HTTPStaticFilesResponse(HTTPResponse):

    def __init__(self, filename, headers=[]):
        if filename.startswith('/'):
            filename = filename[1:]

        self.filename = os.path.join(settings.STATIC_ROOT, filename)
        if not os.path.exists(self.filename):
            super().__init__(status_code=404)
        else:
            super().__init__(status_code=200, headers=headers)

    def get_response_text(self, status_code):
        if status_code == 200:
            with open(self.filename) as staticfile:
                return staticfile.read().encode()

        return super().get_response_text(status_code)

    def get_default_headers(self, status_code):
        if status_code == 200:
            return [('Content-type', mimetypes.guess_type(self.filename)[0])]

        return super().get_default_headers(status_code)


class HTTPTemplateResponse(HTTPResponse):

    def __init__(self, template_name, context={}, headers=[]):
        self.template_name = template_name
        self.context = self.get_context_data(context)
        super().__init__(status_code=200, headers=headers)

    def get_context_data(self, context):
        return context

    def get_response_text(self, status_code):
        if status_code == 200:
            response_text = self.load_template()
            return response_text

        return super().get_response_text()

    def load_template(self):
        project_template_path = os.path.join(
            settings.BASE_DIR, settings.TEMPLATE_DIR, self.template_name
        )
        framework_template_path = os.path.join(
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'templates', self.template_name)
        )
        for path in [project_template_path, framework_template_path]:
            if not os.path.exists(path):
                continue

            with open(path) as template:
                template_text = template.read()
                temp = Template(template_text)
                template_text = temp.substitute(**self.context)

            return template_text.encode()

        raise ValueError(f"Template `{self.template_name}` doesn't exists")
