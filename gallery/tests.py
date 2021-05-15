from django.test import TestCase
from .models import Location,Category,Images
import datetime as dt


# Create your tests here.
class ImagesTestClass(TestCase):
  #setup
  def setUp(self):
    self.location = Location(name='Nairobi')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)

  def test_instance(self):
    self.assertTrue(isinstance,(self.image,Images))

  def test_save_image(self):
    self.image.save_image()
    images=Images.objects.all()
    self.assertTrue(len(images)>0)

  def tearDown(self):
    Images.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()