from myframe.urls import include, static

urlpatterns = {
    '': include('test_app.urls'),
}

urlpatterns.update(static())
