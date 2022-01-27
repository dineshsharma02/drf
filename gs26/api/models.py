from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    # passby = models.CharField(max_length=50)
    passby = models.ForeignKey(User,on_delete=CASCADE)
