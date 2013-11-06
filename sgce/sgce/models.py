# -*- coding: utf-8 -*

from django.db import models
from person.models import Person
from sgce.unislugify import unique_slugify

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
	accept_voucher = models.BooleanField(verbose_name='Aceita Voucher')

	def __unicode__(self):
		return self.name

class Enrollment(models.Model):
	person = models.ForeignKey(Person, verbose_name='Pessoa')
	activities = models.ManyToManyField(Activity, verbose_name='Atividades', related_name='enrollments')
	date = models.DateTimeField(verbose_name='Data')

	def __unicode__(self):
		return self.id

class Event(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=32)
	description = models.CharField(verbose_name='Descrição', max_length=256)
	date = models.DateTimeField(verbose_name='Data')
	local = models.CharField(verbose_name='Local', max_length=64)
	address = models.CharField(verbose_name='Endereço', max_length=512)
	maxpeople = models.DecimalField(verbose_name='Vagas', max_digits=5, decimal_places=0)
	nvouchers = models.DecimalField(verbose_name='Vouchers', max_digits=5, decimal_places=0)
	activities = models.ManyToManyField(Activity, verbose_name='Atividades', null=True, blank=True, related_name='event')
	enrollments = models.ManyToManyField(Enrollment, verbose_name='Inscrições', null=True, blank=True, related_name='event')
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			unique_slugify(self, self.name)
		super(Event, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def people_preview(self):
		return self.enrollments.all().count()

	def people_confirmed(self):
		return self.enrollments.all().count()
