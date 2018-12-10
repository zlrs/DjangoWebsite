from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.welcome, name = 'welcome'),
    path(r'upload', views.upload, name = 'upload'),

]