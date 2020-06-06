from .views import govno_view, dermo_view, template_view, regular_view

urlpatterns = {
    r'^govno/$': govno_view,
    r'^dermo/$': dermo_view,
    r'^template/$': template_view,
    r'^regular/(?P<pk>[0-9]*)/$': regular_view
}
