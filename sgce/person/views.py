# Create your views here.
from django.views.generic.edit import CreateView
from person.models import Person
from person.forms import PersonForm

class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person/signup.html'
    success_url = '/person/login/'
