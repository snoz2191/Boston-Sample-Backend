__author__ = 'domingo'
from rest_framework import serializers
from Tasks.models import *
from django.contrib.auth.models import User

#All of the Serializers of all the models are here

#Login Serializer
class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Login

#Status Serializer
class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = ('code','msg')

# User Serializar
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name','username','email','password')

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    