from myframe.http import HTTPResponse


def govno_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')


def dermo_view(request):
    return HTTPResponse('<h1>Hello from dermo view</h1><p>It is my fucking '
                        'web framework')
