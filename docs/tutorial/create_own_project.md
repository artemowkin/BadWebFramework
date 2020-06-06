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

## Create a new app

To create a new app you need to run this command:

```
$ python manage.py startapp new_app
```

And in your project directory will be created a new `new_app` directory

You can add urls and views in this app, but it's later...
