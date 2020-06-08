from myframe.http import HTTPResponse, HTTPTemplateResponse
from myframe.views import TemplateView, HTMLView


class HelloView(HTMLView):
    html_code = '<h1>Hello World!!!</h1>'


class TemplatePageView(TemplateView):
    template_name = 'template.html'

    def get_context_data(self, request):
        context = super().get_context_data(request)
        data = {'key1': 'val1', 'key2': 'val2'}
        query = request.GET.get('q')
        if not query:
            context['object'] = ''
        else:
            context['object'] = data[query]

        return context


class RegularView(TemplateView):
    template_name = 'regular.html'

    def get_context_data(self, request):
        context = super().get_context_data(request)
        data = {'1': 'foo', '2': 'bar'}
        context['object'] = data.get(self.kwargs['pk'], '')
        return context
