from django.conf.urls import patterns, url
from person import views

urlpatterns = patterns('',
    url(r'^signup/$', views.PersonCreate.as_view(), name='signup'),
)
