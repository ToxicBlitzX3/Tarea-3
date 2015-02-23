from django.conf.urls import patterns, include, url
from misDatos import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
#	url(r'^nombre/$', views.home, name='home'),
 
)