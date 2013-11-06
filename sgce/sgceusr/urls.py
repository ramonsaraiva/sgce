from django.conf.urls import patterns, url
from sgceusr import views

urlpatterns = patterns('',
	url(r'^$', 'sgceusr.views.home', name='home'),
	url(r'^events/$', views.EventList.as_view(), name='events'),
)
