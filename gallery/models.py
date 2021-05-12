from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Location(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Images(models.Model):
  name=models.CharField(max_length=50)
  image=