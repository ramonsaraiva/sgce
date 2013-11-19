# -*- coding: utf-8 -*

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from sgce.models import Event, Activity, Enrollment, Payment, Voucher
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

	def get_context_data(self, **kwargs):
		context = super(EventList, self).get_context_data(**kwargs)
		context['content_title'] = 'Eventos'
		return context

class MyEventList(EventList):
	def get_queryset(self):
		enrollments = Enrollment.objects.filter(person=self.request.user)
		return Event.objects.filter(enrollments__in=enrollments).distinct().order_by('date')

	def get_context_data(self, **kwargs):
		context = super(MyEventList, self).get_context_data(**kwargs)
		context['content_title'] = 'Meus eventos'
		return context

class EventDetail(DetailView):
	model = Event
	template_name = 'sgceusr/event.html'

class ActivityList(ListView):
	model = Activity
	queryset = Activity.objects.order_by('date')
	template_name = 'sgceusr/activities.html'

	def get_context_data(self, **kwargs):
		context = super(ActivityList, self).get_context_data(**kwargs)
		context['content_title'] = 'Atividades'
		return context

class MyActivityList(ActivityList):
	def get_queryset(self):
		enrollments = Enrollment.objects.filter(person=self.request.user)
		return Activity.objects.filter(enrollments__in=enrollments).order_by('date')

	def get_context_data(self, **kwargs):
		context = super(MyActivityList, self).get_context_data(**kwargs)
		context['content_title'] = 'Minhas atividades'
		return context

def enroll(request, slug):
	event = get_object_or_404(Event, slug=slug)

	if request.method == 'POST':
		activities = request.POST.getlist('activities')
		activity_list = get_list_or_404(Activity, id__in=activities)

		form = EnrollmentForm(event.id, activity_list, request.POST)
		if form.is_valid():
			enrollment = Enrollment()
			enrollment.person = request.user
			enrollment.date = datetime.now()
			enrollment.points = form.fields['total_points'].initial
			enrollment.save()

			payment = Payment()
			payment.price = form.fields['total_price'].initial

			token = form.cleaned_data['token']
			if token:
				voucher = Voucher.objects.get(token=token)
				voucher.used = True
				voucher.save()
				payment.price = form.fields['off_price'].initial

			payment.date = datetime.now()
			payment.paid = True
			payment.save()

			enrollment.activities = activity_list
			enrollment.payment = payment
			enrollment.save()

			event.enrollments.add(enrollment)
			event.save()

			messages.success(request, 'Sua inscrição no evento foi realizada com sucesso!')
			return redirect('home')
	elif request.method == 'GET':
		activities = request.GET.getlist('activities')
		activity_list = get_list_or_404(Activity, id__in=activities)
		form = EnrollmentForm(event.id, activity_list, request.GET)

	context = {'event': event, 'activities': activity_list, 'form': form}
	return render(request, 'sgceusr/enroll.html', context)

class PaymentList(ListView):
	model = Payment
	template_name = 'sgceusr/payments.html'

	def get_queryset(self):
		enrollments = Enrollment.objects.filter(person=self.request.user)
		return Payment.objects.filter(enrollment__in=enrollments)
