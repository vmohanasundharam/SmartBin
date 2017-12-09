from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'register', views.register, name='register'),
    url(r'viewbins', views.viewbins, name='viewbins'),
    url(r'map', views.map, name='map'),
    url(r'update', views.update, name='update'),
    url(r'path', views.shortest_path, name='path'),
    url(r'table', views.table, name='table'),
    url(r'put/$', views.update_stats, name='update_stats'),
    url(r'green', views.green_icon, name='green_icon'),
    url(r'red', views.red_icon, name='red_icon'),
    url(r'yellow', views.yellow_icon, name='yellow_icon'),

]
