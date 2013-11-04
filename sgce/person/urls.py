from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from person import views

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name': 'person/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/person/login/'}, name='logout'),
    url(r'^signup/$', views.PersonCreate.as_view(), name='signup'),
)
