from django.conf.urls import patterns,url
from blog import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
	                       url(r'^contact/$', views.contact, name='contact'),)