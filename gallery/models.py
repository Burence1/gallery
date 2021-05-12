from django.db import models
from cloudinary.models import CloudinaryField

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
  image=CloudinaryField('photo')
  description=models.CharField(max_length=100)
  location=models.ForeignKey(Location,on_delete=models.CASCADE)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)

  def __str__(self):
    return self.name