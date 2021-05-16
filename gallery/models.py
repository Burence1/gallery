from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

from django.db.models.fields import DateField

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  @classmethod
  def update_category(cls,id,name):
    cls.objects.filter(id=id).update(name=name)

class Location(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete()

  @classmethod
  def update_location(cls,id,name):
    cls.objects.filter(id=id).update(name=name)

class Images(models.Model):
  name=models.CharField(max_length=50)
  image=CloudinaryField('photo')
  description=models.CharField(max_length=100)
  date=models.DateField(auto_now_add=True)
  location=models.ForeignKey(Location,on_delete=models.CASCADE)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls,id,image):
    update =cls.objects.filter(id=id).update(image=image)
    return update

  @classmethod
  def get_image_by_id(cls,id):
    image=cls.objects.get(id=id)
    return image

  @classmethod
  def search_image(cls,category):
    image=cls.objects.filter(category=category)
    return image
  
  @classmethod
  def get_images(cls):
    return cls.objects.all()

  @classmethod
  def filter_by_location(cls,location):
    located=Location.objects.get(name=location)
    image=Images.objects.filter(location=located.id)
    return image

  class Meta:
    ordering = ['date']