from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from sgce.models import Event, Activity
from sgceusr.forms import EnrollmentForm

def home(request):
	return render(request, 'sgceusr/home.html')

class EventList(ListView):
	model = Event
	queryset = Event.objects.order_by('date')
	template_name = 'sgceusr/events.html'

class EventDetail(DetailView):
	model = Event
	template_name = 'sgceusr/event.html'

class ActivityList(ListView):
	model = Activity
	template_name = 'sgceusr/activities.html'


def enroll(request, slug):
	event = get_object_or_404(Event, slug=slug)
	activities = request.GET.getlist('activities')
	activity_list = get_list_or_404(Activity, id__in=activities)
	total_price = sum(a.price for a in activity_list)
	total_points = sum(a.points for a in activity_list)

	if request.method == 'POST':
		a = 'a'

	context = {'event': event, 'activities': activity_list, 'total_price': total_price, 'total_points': total_points}
	return render(request, 'sgceusr/enroll.html', context)
