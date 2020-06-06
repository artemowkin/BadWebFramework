import os

from myframe.settings import settings


class HTTPRequest:

    def __init__(self, environ):
        self.path = environ['PATH_INFO']
        self.cookies = environ.get('HTTP_COOKIE', '')


class HTTPResponse:

    def __init__(self, text='', status_code=200, headers=[]):
        if status_code != 200 and text:
            raise ValueError(
                f'You cannot setup text to {status_code} status code'
            )
        self.status = self.get_response_status(status_code)
        self.response_text = (text.encode() or
                              self.get_response_text(status_code))
        self.headers = headers or self.get_default_headers()

    def get_response_status(self, status_code):
        if status_code == 200:
            return '200 OK'
        elif status_code == 404:
            return '404 Not Found'
        elif status_code == 301:
            return '301 Moved Permanently'

    def get_response_text(self, status_code):
        if status_code == 404:
            return '<h1>404 Not Found</h1>'.encode()

        return ''.encode()

    def get_default_headers(self):
        return [('Content-type', 'text/html')]


class HTTPTemplateResponse(HTTPResponse):

    def __init__(self, template_name, context={}, status_code=200,
                 headers=[]):
        self.template_name = template_name
        self.context = self.get_context_data(context)
        super().__init__(status_code=status_code, headers=headers)

    def get_context_data(self, context):
        return context

    def get_response_text(self, status_code):
        if status_code == 200:
            response_text = self.load_template()
            return response_text

        return super().get_response_text()

    def load_template(self):
        template_path = os.path.join(
            settings.BASE_DIR, settings.TEMPLATE_DIR, self.template_name
        )
        if not os.path.exists(template_path):
            raise ValueError(f"Template `{template_path}` does not exists")

        with open(template_path) as template:
            template_text = template.read()
            template_text = template_text.format(**self.context)

        return template_text.encode()
