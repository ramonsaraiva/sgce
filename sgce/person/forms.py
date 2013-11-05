from django import forms
from person.models import Person
import pdb

class PersonForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	class Meta:
		model = Person
		widgets = {'password': forms.PasswordInput}
		exclude = ['stype', 'last_login', 'date_joined']

	def save(self):
		pdb.set_trace()
		person = super(PersonForm, self).save(commit=False)
		person.set_password(self.cleaned_data["password"])
		person.is_active = True

		person.save()
		return person
