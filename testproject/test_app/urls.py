from .views import hello_view, template_view, regular_view

urlpatterns = {
    r'^hello/$': hello_view,
    r'^template/$': template_view,
    r'^regular/(?P<pk>[0-9]*)/$': regular_view
}
