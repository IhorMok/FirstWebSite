from django.urls import path, re_path
from . import views
from .models import Articles
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.show),
    path('download', views.download, name='download'),
    path('contact', views.contact, name='contact'),
    re_path(r'^favicon\.ico$', favicon_view),

]
