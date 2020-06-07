# Tutorial: Create Own Project

If you want to create your own project you can do it in repo directory

Ok, let's create new `my_project` project

```
$ python -m myframe.myframeadmin startproject my_project
```

Now you can see new directory `my_project`. Let's start this project

```
$ cd my_project
$ gunicorn my_project.wsgi
```

And visit http://localhost:8000/

## Create a new page

Let's add a new page that will be tell us "Hello World!!!"

### Pages app

First of all we need to create a new app `pages` for our code. To create this app you need to run this command:

```
$ python manage.py startapp pages
```

### URLs

To add a new URL route we need to include our app in project-level `urls.py` first. Let's do that. Change `my_project/urls.py` file:

```python
from myframe.urls import include

urlpatterns = {
    '': include('pages.urls'),
}
```

Now we can add URL routes in our app. Let's add new `hello/` route in `pages/urls.py` file:

```python
from .views import hello_view

urlpatterns = {
    'hello/': hello_view
}
```

### Views

We import `hello_view`, but we don't create it. Let's fix it. Change `pages/views.py` file

```python
from myframe.http import HTTPResponse


def hello_view(request):
    return HTTPResponse('<h1>Hello World!!!</h1>')
```

And it's all. Run the server, visit http://localhost:8000/hello/, and you will see "Hello World!!!" message

```
$ gunicorn my_project.wsgi
```
