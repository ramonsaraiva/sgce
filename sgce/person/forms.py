from django import forms
from person.models import Person

class PersonForm(forms.ModelForm):
	def init(self, *args, **kwargs):
		super(PlayerForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	class Meta:
		model = Person
		widgets = {'password': forms.PasswordInput}
		exclude = ['last_login', 'date_joined']

		def save(self):
			person = super(PersonForm, self).save(commit=False)
			person.set_password(self.cleaned_data["password"])
			person.is_active = True

			player.save()
			return player
