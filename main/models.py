from django.db import models

# Create your models here.
class Animal(models.Model):
  nome_animal = models.CharField(max_length=256)
  data_nascimento = models.DateField(null=True)
  ativo = models.BooleanField(default=True)
