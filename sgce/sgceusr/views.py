from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from sgce.models import Event

def home(request):
	return render_to_response('sgceusr/home.html', RequestContext(request))

class EventList(ListView):
	model = Event
	template_name = 'sgceusr/events.html'
