from myframe.urls import include, StaticFilesHandler

urlpatterns = {
    '': include('test_app.urls'),
    'static/': StaticFilesHandler.as_view(),
}
