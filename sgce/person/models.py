from django.db import models
from django.db.models import Count
from django.contrib.auth.models import AbstractUser
from sgce.models import Enrollment, Event

class Person(AbstractUser):
	MALE = 'M'
	FEMALE = 'F'

	SEX_CHOICES = (
		(MALE, 'M'),
		(FEMALE, 'F'),
	)

	PARTICIPANT = 'P'
	OPERATOR = 'O'
	RECEPTIONIST = 'R'

	STYPE_CHOICES = (
		(PARTICIPANT, 'Participante'),
		(OPERATOR, 'Operador'),
		(RECEPTIONIST, 'Recepcionista'),
	)

	name = models.CharField(verbose_name='Nome', max_length=30)
	cpf = models.CharField(verbose_name='CPF', max_length=11)
	nationality = models.CharField(verbose_name='Nacionalidade', max_length=64)
	sex = models.CharField(verbose_name='Sexo', max_length=1, choices=SEX_CHOICES, default=MALE)
	scholarity = models.CharField(verbose_name='Escolaridade', max_length=32)
	birth = models.DateField(verbose_name='Data de nascimento')
	stype = models.CharField(max_length=1, choices=STYPE_CHOICES, default=PARTICIPANT)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['name', 'email', 'cpf', 'nationality', 'sex', 'scholarity', 'birth']

	def __unicode__(self):
		return self.username

	def nof_events_enrolled(self):
		enrollments = Enrollment.objects.filter(person=self)
		return Event.objects.filter(enrollments__in=enrollments).distinct().count()

	def nof_activities_enrolled(self):
		act = 0
		for enrollment in Enrollment.objects.filter(person=self).annotate(act_count=Count('activities__id', distinct=True)):
			act += enrollment.act_count
		return act
