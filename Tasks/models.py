from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Login
class Login(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=16)


# Status
class Status(models.Model):
  code = models.CharField(max_length=20)
  msg = models.CharField(max_length=50)

class Task(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  creator = models.ForeignKey(User,to_field='username') 
