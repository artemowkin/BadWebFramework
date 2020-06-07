# Tutorial: Render Templates

How about templates? Can i render HTML code from file? Offcourse. Let's do that

## Template Page

In previous guide we create `pages` app. In this guide we continue to work with this app and create new page that will be render a simple html file

To do that we need to create a new URL, View and Template. Let's start with URL. Change the `pages/urls.py` file:

```python
from .views import hello_view, template_view

urlpatterns = {
    'hello/': hello_view,
    'template/': template_view,
}
```

Ok, now we need to create new `template_view` view. Change the `pages/views.py` file

```python
from myframe.http import HTTPResponse, HTTPTemplateResponse


def hello_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')


def template_view(request):
    return HTTPTemplateResponse(template_name='template.html')
```

And now we need to create the `template.html` template. In our project we can see the `templates` directory. This framework looks for templates in this dir. And we need to add into this directory `template.html` template. Let's do that

```
$ touch templates/template.html
```

And in this file we add some HTML code:

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Template Page</title>
    </head>
    <body>
        <h1>Template Page</h1>
        <p>Hello from template page. This page is a loaded HTML file. Wooho!!!</p>
    </body>
</html>
```

Run the server

```
$ gunicorn my_project.wsgi
```

And visit http://localhost:8000/template/

## Class-Based TemplateView

But you can use class instead functions. Let's change our function-based view `template_view` to class-based `TemplatePageView`. Change `pages/views.py` file:

```python
from myframe.http import HTTPResponse, HTTPTemplateResponse
from myframe.views import TemplateView


def hello_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')


class TemplatePageView(TemplateView):
    template_name = 'template.html'
```

And we need to change `pages/urls.py`

```python
from .views import hello_view, TemplatePageView

urlpatterns = {
    'hello/': hello_view,
    'template/': TemplatePageView.as_view(),
}
```

Nothing has changed, but the text has become smaller
