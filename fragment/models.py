from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'user'

class Task(models.Model):
    task = models.CharField(max_length=150, blank=False)
    day = models.CharField(max_length=150, blank=False)
    hour = models.CharField(max_length=150, blank=False)
    note = models.CharField(max_length=150, blank=False)

    class Meta:
        db_table = 'tasks'