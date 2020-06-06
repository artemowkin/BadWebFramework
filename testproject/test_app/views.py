from myframe.http import HTTPResponse, HTTPTemplateResponse


def hello_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')


def template_view(request):
    data = {'key1': 'val1', 'key2': 'val2'}
    return HTTPTemplateResponse('template.html', context=data)


def regular_view(request, pk):
    data = {'1': 'foo', '2': 'bar'}
    context_data = {'object': data.get(pk, '')}
    return HTTPTemplateResponse('regular.html', context=context_data)
