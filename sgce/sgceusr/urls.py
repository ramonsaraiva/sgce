from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'sgceusr.views.home', name='home'),
)
