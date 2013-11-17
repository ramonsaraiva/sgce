from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from sgce.models import Event, Activity, Enrollment, Payment
from sgceusr.forms import EnrollmentForm
from datetime import datetime

def home(request):
	enrollments = Enrollment.objects.filter(person=request.user)
	events = Event.objects.filter(enrollments__in=enrollments).distinct().order_by('date')
	activities = Activity.objects.filter(enrollments__in=enrollments).order_by('date')

	context = {'events': events, 'activities': activities}
	return render(request, 'sgceusr/home.html', context)

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

	if request.method == 'POST':
		activities = request.POST.getlist('activities')
		activity_list = get_list_or_404(Activity, id__in=activities)
		total_price = sum(a.price for a in activity_list)
		total_points = sum(a.points for a in activity_list)

		enrollment = Enrollment()
		enrollment.person = request.user
		enrollment.date = datetime.now()
		enrollment.points = total_points

		enrollment.save()

		payment = Payment()
		payment.price = total_price
		payment.date = datetime.now()
		payment.paid = True
		payment.save()

		enrollment.activities = activity_list
		enrollment.payment = payment

		enrollment.save()

		event.enrollments.add(enrollment)
		event.save()

		return redirect('home')

	activities = request.GET.getlist('activities')
	activity_list = get_list_or_404(Activity, id__in=activities)
	total_price = sum(a.price for a in activity_list)
	total_points = sum(a.points for a in activity_list)

	context = {'event': event, 'activities': activity_list, 'total_price': total_price, 'total_points': total_points}
	return render(request, 'sgceusr/enroll.html', context)
