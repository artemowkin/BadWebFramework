# Run test project

To run built in test project you need to install pipenv (if it's not installed), sync all dependencies, and run shell

```
$ pipenv sync
$ pipenv shell
```

Change your directory to `testproject`

```
$ cd testproject
```

And run gunicorn web server

```
$ gunicorn proj.wsgi
```

# Docs

If you want to work with my (bad (really!)) framework you can read documentation into `docs` directory
