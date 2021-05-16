from gallery.views import category
from django.test import TestCase
from .models import Location,Category,Images
import datetime as dt
import tempfile
from django.test import override_settings


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

  def test_delete_image(self):
    self.image.save_image()
    images=Images.objects.all()
    self.assertEqual(len(images),1)
    self.image.delete_image()
    del_images=Images.objects.all()
    self.assertEqual(len(del_images),0)

  # @override_settings(MEDIA_ROOT=tempfile.gettempdir())
  # def test_update_image(self):
  #   self.image.save_image()
  #   self.image.update_image(self.image.id,"new.png")
  #   update=Images.objects.get(image="new.png")
  #   self.assertEqual(update.image,"new.png")

  def test_search_category(self):
    self.location = Location(name='Nairobi')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)
    self.image.save_image()
    images=Images.search_image(self.category.id)
    self.assertTrue(len(images) > 0)

  def test_filter_location(self):
    self.location = Location(name='chuka')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)
    self.image.save_image()
    images = Images.filter_by_location("chuka")
    self.assertTrue(len(images) > 0)

  def test_get_image_by_id(self):
    self.location = Location(name='chuka')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)
    self.image.save_image()
    images = Images.get_image_by_id(self.image.id)
    self.assertEqual(images.name, self.image.name)

  def test_display_images(self):
    self.image.save_image()
    images=Images.get_images()
    self.assertEqual(len(images), 1)

class CategoryTest(TestCase):
  def setUp(self):
    self.tech = Category(name='tech')
    self.food=Category(name='food')
    self.fitness=Category(name='fitness')

  def tearDown(self):
    Category.objects.all().delete()

  def test_save_category(self):
    self.food.save_category()
    self.fitness.save_category()
    self.tech.save_category()
    category=Category.objects.all()
    self.assertEqual(len(category),3)