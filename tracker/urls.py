from django.conf.urls import url
from . import views

app_name = 'tracker'

urlpatterns = [
    url(r'^index/$', views.index, name = 'index'),
    url(r'^log/$', views.log, name = 'log'),
]