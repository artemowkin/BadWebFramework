import os
import sys


def create_empty_file(directory, file_name):
    open(os.path.join(directory, file_name), 'a').close()


def create_file(directory, file_name, text):
    with open(os.path.join(directory, file_name), 'w') as f:
        f.write(text)


def startapp(app_name):
    if os.path.exists(app_name):
        raise ValueError(f"`{app_name}` app exists")

    base_dir = os.path.abspath('.')
    app_dir = os.path.join(base_dir, app_name)

    # app directory
    os.mkdir(app_dir)

    # __init__.py
    create_empty_file(app_dir, '__init__.py')

    # urls.py
    create_file(app_dir, 'urls.py',
                "urlpatterns = {\n\t# Url patterns here\n}")

    # views.py
    create_file(app_dir, 'views.py',
                "from myframe.http import HTTPResponse\n\n"
                "# Your views here\n")


def startproject(project_name, path=''):
    if not path:
        path = project_name

    if os.path.exists(path) and path != '.':
        raise ValueError(f"Directory `{path}` exists")

    if path != '.':
        os.mkdir(path)

    base_dir = os.path.abspath(path)
    main_project_app = os.path.join(base_dir, project_name)

    # main project app
    os.mkdir(main_project_app)

    # manage.py
    create_file(base_dir, 'manage.py',
                "import os\nimport sys\n\n"
                f"from {project_name}.settings import BASE_DIR\n\n"
                "sys.path.append(os.path.dirname(BASE_DIR))\n\n"
                "from myframe.myframeadmin import run_command\n\n"
                "os.environ.setdefault('MYFRAME_SETTINGS_MODULE',"
                f"'{project_name}.settings')\n\n"
                "run_command(*sys.argv)")

    # templates dir
    os.mkdir(os.path.join(base_dir, 'templates'))

    # static dir
    os.mkdir(os.path.join(base_dir, 'static'))

    # __init__.py
    create_empty_file(main_project_app, '__init__.py')

    # settings.py
    create_file(main_project_app, 'settings.py',
                f"import os\n\nROOT_URLCONF = '{project_name}.urls'\n\n"
                "BASE_DIR = os.path.dirname(os.path.dirname"
                "(os.path.abspath(__file__)))\n\n"
                "TEMPLATE_DIR = 'templates'\n\nSTATIC_URL='/static/'\n\n"
                "STATIC_ROOT = os.path.join(BASE_DIR, 'static')")

    # urls.py
    create_file(main_project_app, 'urls.py',
                "from myframe.urls import include\n\nurlpatterns = {\n\t"
                "# Here must be url patterns like this:\n\t"
                "# '': include('app.urls')\n}")

    # wsgi.py
    create_file(main_project_app, 'wsgi.py',
                "import sys\nimport os\n\nfrom .settings import BASE_DIR\n\n"
                "os.environ.setdefault('MYFRAME_SETTINGS_MODULE', "
                f"'{project_name}.settings')\n\n"
                "sys.path.append(os.path.dirname(BASE_DIR))\n\n"
                "from myframe.wsgi import get_wsgi_application\n\n"
                "application = get_wsgi_application()")


def run_command(app_name, command='', *args):
    commands_help = """
    To start new project you can run startproject command

        $ python -m myframe.myframeadmin startproject test_project

    To start new app you can run startapp command from project directory

        $ python manage.py startapp application

    To watch this text you can do this

        $ python manage.py --help


    It follows these commands:

        startproject <project_name> [<path>]

            project_name - name of the project

            path = it isn't required path/name of directory of the project

        startapp <app_name>

            app_name - name of the app
    """
    if command == 'startproject':
        if 'manage.py' in app_name:
            raise ValueError("You can't start new project because you're "
                             "now in the project")

        startproject(*args)
    elif command == 'startapp':
        startapp(*args)
    else:
        print(commands_help)


if __name__ == '__main__':
    run_command(*sys.argv)
