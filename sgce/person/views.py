# -*- coding: utf-8 -*

from django.views.generic.edit import CreateView
from person.models import Person
from person.forms import PersonForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

class PersonCreate(CreateView):
	model = Person
	form_class = PersonForm
	template_name = 'person/signup.html'
	success_url = '/person/login/'

def login(request):
	context = {}

	if request.method == 'POST':
		auth_logout(request)

		username = request.POST['username']
		password = request.POST['password']

		if not request.user.is_authenticated():
			user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				auth_login(request, user);

				if user.stype == 'P':
					return redirect('/sgceusr/')
				elif user.stype == 'O' or user.stype == 'R':
					return redirect('/sgceman/')
			else:
				context['error'] = 'Usuário inativo'
		else:
			context['error'] = 'Usuário ou senha incorretos'

	return render_to_response('person/login.html', context, RequestContext(request))
