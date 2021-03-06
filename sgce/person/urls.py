from django.conf.urls import patterns, url, include
from django.contrib.auth.views import logout
from person import views

urlpatterns = patterns('',
    url(r'^login/$', 'person.views.login', name='login'),
    url(r'^logout/$', logout, {'next_page': '/person/login/'}, name='logout'),
    url(r'^signup/$', views.PersonCreate.as_view(), name='signup'),
)
