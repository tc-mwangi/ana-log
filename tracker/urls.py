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
    url(r'^ajax/my_ajax_request/$', views.requestAjax, name='requestAjax'),
    
    url(r'^tasksapi$', views.TaskList.as_view()),

    # test ajax urls
    url(r'^foo', views.foo, name='foo'),
    url(r'^mygetview', views.mygetview, name='mygetview'),
    url(r'^mypostview', views.mypostview, name='mypostview'),
    url(r'^myajaxview', views.myajaxview, name='myajaxview'),
    url(r'^myajaxformview', views.myajaxformview, name='myajaxformview'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






