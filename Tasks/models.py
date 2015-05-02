from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


# Create your models here.

# Login
class Login(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=16)

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Login

# Status
class Status(models.Model):
  code = models.CharField(max_length=10)
  msg = models.CharField(max_length=50)

class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = ('code','msg')
# User
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username','email','password')