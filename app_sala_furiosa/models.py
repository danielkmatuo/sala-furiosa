from django.db import models
from datetime import datetime

# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length = 1000)

class Mensagem(models.Model):
    username = models.CharField(max_length = 1000)
    sala = models.CharField(max_length = 1000)
    texto = models.CharField(max_length = 1000000)
    data = models.DateTimeField(default = datetime.now, blank = True)