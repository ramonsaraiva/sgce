from django.conf.urls import patterns, include, url
from sgce import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sgce.views.switch', name='switch'),
    url(r'^person/', include('person.urls')),
	url(r'^sgceusr/', include('sgceusr.urls')),
	#url(r'^sgceman/', include('sgceman.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
