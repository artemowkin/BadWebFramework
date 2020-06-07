from .views import HelloView, TemplatePageView, RegularView

urlpatterns = {
    r'^hello/$': HelloView.as_view(),
    r'^template/$': TemplatePageView.as_view(),
    r'^regular/(?P<pk>[0-9]*)/$': RegularView.as_view()
}
