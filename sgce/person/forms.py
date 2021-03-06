from django import forms
from person.models import Person

class PersonForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	class Meta:
		model = Person
		widgets = {'password': forms.PasswordInput}
		exclude = ['is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name', 'is_staff', 'is_active', 'stype', 'last_login', 'date_joined', ]

	def save(self):
		person = super(PersonForm, self).save(commit=False)
		person.set_password(self.cleaned_data["password"])
		person.is_active = True

		person.save()
		return person
