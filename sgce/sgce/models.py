# -*- coding: utf-8 -*

from django.db import models
from sgce.unislugify import unique_slugify
from randomslugfield import RandomSlugField

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

class Payment(models.Model):
	price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
	date = models.DateTimeField(verbose_name='Data')
	paid = models.BooleanField(verbose_name='Pago', default=False)

	def __unicode__(self):
		return self.enrollment.person.name

class Enrollment(models.Model):
	person = models.ForeignKey('person.Person', verbose_name='Pessoa')
	activities = models.ManyToManyField(Activity, verbose_name='Atividades', related_name='enrollments')
	payment = models.OneToOneField(Payment, verbose_name='Pagamento', blank=True, null=True, related_name='enrollment')
	date = models.DateTimeField(verbose_name='Data')
	points = models.DecimalField(verbose_name='Pontos', max_digits=5, decimal_places=0)

	def __unicode__(self):
		return self.person.name

class Voucher(models.Model):
	token = RandomSlugField(length=5, unique=True)
	used = models.BooleanField(verbose_name='Utilizado', default=False)

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
	vouchers = models.ManyToManyField(Voucher, verbose_name='Vouchers', null=True, blank=True, related_name='event')
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			unique_slugify(self, self.name)

		super(Event, self).save(*args, **kwargs)

		for i in range(self.nvouchers):
			v = Voucher()
			v.save()
			self.vouchers.add(v)

	def __unicode__(self):
		return self.name

	def people_preview(self):
		return self.enrollments.all().count()

	def people_confirmed(self):
		return self.enrollments.all().count()
