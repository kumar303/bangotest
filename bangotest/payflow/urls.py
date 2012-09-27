from django.conf.urls.defaults import *

from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='payflow.home'),
    url(r'^process$', views.process, name='payflow.process'),
)
