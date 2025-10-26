from django.urls import path, re_path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.floor_default, name='home'),
    re_path(r'^floor/(?P<number>-?[0-9]+)/$', views.floor_detail, name='floor_detail'),
]
