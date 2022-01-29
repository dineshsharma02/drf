from django.db import models
from django.forms import CharField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()