from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from sgce.models import Event, Activity

def home(request):
	return render_to_response('sgceusr/home.html', RequestContext(request))

class EventList(ListView):
	model = Event
	template_name = 'sgceusr/events.html'

class EventDetail(DetailView):
	model = Event
	template_name = 'sgceusr/event.html'

class ActivityList(ListView):
	model = Activity
	template_name = 'sgceusr/activities.html'
