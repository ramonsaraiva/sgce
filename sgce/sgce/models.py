# -*- coding: utf-8 -*

from django.db import models

class Activity(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=32)
	description = models.CharField(verbose_name='Descrição', max_length=256)
	date = models.DateTimeField(verbose_name='Data')
	local = models.CharField(verbose_name='Local', max_length=64)
	address = models.CharField(verbose_name='Endereço', max_length=512)
	maxpeople = models.DecimalField(verbose_name='Vagas', max_digits=5, decimal_places=0)
	charge = models.DecimalField(verbose_name='Carga Horária', max_digits=10, decimal_places=2)
	points = models.DecimalField(verbose_name='Pontos para participante', max_digits=5, decimal_places=0)
	price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
	accept_group_off = models.BooleanField(verbose_name='Aceita desconto por grupo')
	accept_voucher = models.BooleanField(verbose_name='Aceita Voucher')

	def __unicode__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=32)
	description = models.CharField(verbose_name='Descrição', max_length=256)
	date = models.DateTimeField(verbose_name='Data')
	local = models.CharField(verbose_name='Local', max_length=64)
	address = models.CharField(verbose_name='Endereço', max_length=512)
	maxpeople = models.DecimalField(verbose_name='Vagas', max_digits=5, decimal_places=0)
	nvouchers = models.DecimalField(verbose_name='Vouchers', max_digits=5, decimal_places=0)
	activities = models.ManyToManyField(Activity)

	def __unicode__(self):
		return self.name

