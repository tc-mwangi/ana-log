from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import requestAjax
from django.urls import path

app_name = 'tracker'

urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^log/$', views.log, name = 'log'),
    path('my_ajax_request', requestAjax, name='my_ajax_request'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)