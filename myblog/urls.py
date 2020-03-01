from django.urls import path, re_path
from . import views
from .models import Articles
from django.views.generic import RedirectView
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.show),
    path('download', views.download, name='download'),
    path('contact', views.contact, name='contact'),

]
