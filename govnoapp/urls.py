from .views import govno_view, dermo_view

urlpatterns = {
    'govno/': govno_view,
    'dermo/': dermo_view,
}
