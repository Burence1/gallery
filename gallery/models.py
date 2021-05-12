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

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls,id,image):
    update =cls.objects.filter(id=id).update(image=image)

  @classmethod
  def get_image_by_id(cls,id):
    image=cls.objects.get(id=id)
    return image

  @classmethod
  def search_image(cls,category):
    