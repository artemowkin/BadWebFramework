from myframe.http import HTTPResponse, HTTPTemplateResponse


def govno_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')


def dermo_view(request):
    return HTTPResponse('<h1>Hello from dermo view</h1><p>It is my fucking '
                        'web framework')


def template_view(request):
    return HTTPTemplateResponse('template.html')
