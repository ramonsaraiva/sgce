# -*- coding: utf-8 -*

from django import forms
from sgce.models import Event
from decimal import Decimal

class EnrollmentForm(forms.Form):
	event_id = forms.CharField(required=False)
	total_price = forms.DecimalField(required=False)
	off_price = forms.DecimalField(required=False)
	total_points = forms.DecimalField(required=False)
	token = forms.CharField(max_length=5, required=False)
	cc_number = forms.CharField(required=False)
	cc_date = forms.CharField(required=False)
	cc_cod = forms.CharField(max_length=3, required=False)

	def __init__(self, event_id, activities, *args, **kwargs):
		super(EnrollmentForm, self).__init__(*args, **kwargs)
		self.fields['event_id'].initial = event_id
		self.fields['activities'] = forms.MultipleChoiceField(choices=[ (a.id, a.name) for a in activities])
		self.fields['total_price'].initial = sum(a.price for a in activities)
		self.fields['off_price'].initial = self.fields['total_price'].initial - self.fields['total_price'].initial * Decimal('0.2')
		self.fields['total_points'].initial = sum(a.points for a in activities)

	def clean_token(self):
		data = self.cleaned_data['token']
		event = Event.objects.get(id=self.fields['event_id'].initial)

		if not data:
			return data

		try:
			voucher = event.vouchers.get(token=data)
		except:
			raise forms.ValidationError("Voucher inválido, verifique se o token foi digitado corretamente.")
		if voucher.used:
			raise forms.ValidationError("O voucher especificado já está em uso, verifique se o token foi digitado corretamente.")

		return data
