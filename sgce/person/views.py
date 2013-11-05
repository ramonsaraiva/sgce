# Create your views here.
from django.views.generic.edit import CreateView
from person.models import Person
from person.forms import PersonForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login as core_login

class PersonCreate(CreateView):
	model = Person
	form_class = PersonForm
	template_name = 'person/signup.html'
	success_url = '/person/login/'

def login(request):
	if request == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username, password)

		if user is not None:
			if user.is_active:
				if user.stype == 'P':
					#redirects to participant page
					return
				elif user.stype == 'O' or user.stype == 'R':
					#redirects to operators/receptionists page
					return
			else:
				#not active error
				return
		else:
			#credentials error
			return

		return
	#just for now..
	return core_login(request, 'person/login.html')
