from django import forms
from sgce.models import Activity

class EnrollForm(forms.Form):
	activities = forms.ModelMultipleChoiceField(Activity.objects.none())
