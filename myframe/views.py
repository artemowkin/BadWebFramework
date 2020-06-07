from myframe.http import HTTPResponse, HTTPTemplateResponse


class View:
    http_methods = ['get', 'post', 'put', 'patch', 'delete', 'head',
                    'options', 'trace']

    def __init__(self, **kwargs):
        for arg, val in kwargs.items():
            setattr(self, arg, val)

    @classmethod
    def as_view(cls, **initkwargs):
        for key in initkwargs:
            if arg in self.http_methods:
                raise ValueError(f"`{arg}` is a name of view method")

            if not hasattr(cls, key):
                raise ValueError(f"`{cls.__name__}` doesn't have `{key}` "
                                 "attribute")

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):
                raise ValueError(f"View doesn't have request attribute. You "
                                 "can forgot to run super().setup()")

            return self.dispatch(request, *args, **kwargs)

        return view

    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_methods:
            handler = getattr(self, request.method.lower())
        else:
            handler = self.http_method_not_allowed()

        return handler(request, *args, **kwargs)

    def http_method_not_allowerd(self):
        return HTTPResponse(status_code=405)


class TemplateView(View):
    template_name = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return self.render_to_response(context)

    def get_context_data(self, request):
        return {'request': request}

    def render_to_response(self, context):
        if not self.template_name:
            raise ValueError(f"You need to set `template_name` attribute")

        return HTTPTemplateResponse(template_name=self.template_name,
                                    context=context)


class HTMLView(View):
    html_code = None

    def get(self, request, *args, **kwargs):
        if not self.html_code:
            raise ValueError(f"You need to set `html_code` attribute")

        return HTTPResponse(text=self.html_code)
