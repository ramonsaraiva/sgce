from django.db import models

class Event(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=32)
	description = models.CharField(verbose_name='Descrição', max_length=256)
	date = models.DateField(verbose_name='Data')
	time = models.TimeField(verbose_name='Hora')
	local = models.CharField(verbose_name='Local', max_length=64)
	address = models.CharField(verbose_name='Endereço', max_length=512)
	maxpeople = models.DecimalField(verbose_name='Vagas',..)
	nvouchers = models.DecimalField(verbose_name='Vouchers',..)
	activities = models.ManyToManyField(Activity)

	def __unicode__(self):
		return self.name

class Activity(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=32)
	description = models.CharField(verbose_name='Descrição', max_length=256)
	date = models.DateField(verbose_name='Data')
	time = models.TimeField(verbose_name='Hora')
	local = models.CharField(verbose_name='Local', max_length=64)
	address = models.CharField(verbose_name='Endereço', max_length=512)
	maxpeople = models.DecimalField(verbose_name='Vagas',..)
	charge = models.DecimalField(verbose_name='Carga Horária', ..)
	points = models.DecimalField(verbose_name='Pontos para participante', ..)
	price = models.DecimalField(verbose_name='Price', ..)
	accept_group_off = models.BooleanField(verbose_name='Aceita desconto por grupo')
	accept_voucher = models.BooleanField(verbose_name='Aceita Voucher')

	def __unicode__(self):
		return self.name
