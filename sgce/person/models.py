from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'

    SEX_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    name = models.CharField(verbose_name='Nome', max_length=30)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    nationality = models.CharField(verbose_name='Nacionalidade', max_length=64)
    sex = models.CharField(verbose_name='Sexo', max_length=1, choices=SEX_CHOICES, default=MALE)
    sholarity = models.CharField(verbose_name='Escolaridade', max_length=32)
    birth = models.DateField(verbose_name='Data de nascimento')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'cpf', 'nacionality', 'sex', 'scholarity', 'birth']
