import importlib


def include(app_urls):
    urls_module = importlib.import_module(app_urls)
    if not hasattr(urls_module, 'urlpatterns'):
        raise ValueError(f"{url_module} module doesn't have `urlpatterns`")

    return urls_module.urlpatterns
