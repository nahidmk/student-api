from django.db import models

# Create your models here.

class Student(models.Model):
    s_id = models.IntegerField()
    name = models.CharField(max_length=70)
    batch = models.IntegerField()
    dep = models.CharField(max_length=10)

class Registration(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)
