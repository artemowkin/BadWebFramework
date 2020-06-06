# Tutorial: Testing Project

After installing dependencies you can play with testing project. Let's run it

First of all you need to change your directory

```
$ cd testproject
```

Ok. Now we can run this project

```
$ gunicorn proj.wsgi
```

You need to visit http://localhost:8000/

This project has three pages:

* `hello/` - simple page that returns `Hello World` message
* `template/` - page that render template `template.html`
* `regular/<id>/` - page that return data for this id
