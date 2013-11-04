from django.conf.urls import patterns, include, url
from sgce import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.SwitchView.as_view(), name='switch'),
    url(r'^person/', include('person.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
