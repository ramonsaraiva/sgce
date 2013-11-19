from django.conf.urls import patterns, url
from sgceusr import views

urlpatterns = patterns('',
	url(r'^$', 'sgceusr.views.home', name='home'),
	url(r'^account/$', views.AccountUpdate.as_view(), name='account'),
	url(r'^events/$', views.EventList.as_view(), name='events'),
	url(r'^events/enrolled/$', views.MyEventList.as_view(), name='events-enrolled'),
	url(r'^events/(?P<slug>[\w\-]+)/$', views.EventDetail.as_view(), name='event'),
	url(r'^events/(?P<slug>[\w\-]+)/enroll$', 'sgceusr.views.enroll', name='enroll'),
	url(r'^activities/$', views.ActivityList.as_view(), name='activities'),
	url(r'^activities/enrolled/$', views.MyActivityList.as_view(), name='activities-enrolled'),
	url(r'^payments/$', views.PaymentList.as_view(), name='payments'),
)
