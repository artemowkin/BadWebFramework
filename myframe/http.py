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
        elif status_code == 200 and not text:
            raise ValueError(
                f'You need to setup text for 200 status code'
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
