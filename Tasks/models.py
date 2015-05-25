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

# Task
class Task(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  creator = models.ForeignKey(User,to_field='username')

  def __unicode__(self):
    return self.name
 
# Execution
class Execution(models.Model):
  
  # Defines Difficulty Choices
  EASY = 0 
  MEDIUM = 1
  HARD = 2
    
  DIFFICULTY_CHOICES = (
    (EASY,'easy'),
    (MEDIUM,'medium'),
    (HARD,'hard'),
  )

  # Defines Status Choices
  PENDING = 2
  CANCELED = 1
  DONE = 0  

  STATUS_CHOICES = (
    (PENDING,'pending'),
    (CANCELED,'canceled'),
    (DONE,'done'),
  )

  date = models.DateTimeField()
  comment = models.TextField()
  difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=EASY)
  duration = models.IntegerField()
  status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
  executioner = models.ForeignKey(User, to_field='username')
  task_associated = models.ForeignKey(Task)
