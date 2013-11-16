from django import forms

class EnrollmentForm(forms.Form):
	def __init__(self, event, activities, *args, **kwargs):
		super(EnrollmentForm, self).__init__(*args, **kwargs)
		self.fields['activities'] = forms.ChoiceField(choices=[ (a.id, a.name) for a in activities])
