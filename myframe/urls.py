import importlib

from myframe.views import View
from myframe.settings import settings
from myframe.http import HTTPStaticFilesResponse


class StaticFilesHandler(View):

    def get(self, request, *args, **kwargs):
        if not request.path.startswith(settings.STATIC_URL):
            raise ValueError("You set uncorrect `static_url`")

        staticfile = request.path[len(settings.STATIC_URL):]
        return HTTPStaticFilesResponse(staticfile)


def include(app_urls):
    urls_module = importlib.import_module(app_urls)
    if not hasattr(urls_module, 'urlpatterns'):
        raise ValueError(f"{url_module} module doesn't have `urlpatterns`")

    return urls_module.urlpatterns
