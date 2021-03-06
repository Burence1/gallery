from django.test import TestCase
from .models import Location,Category,Images


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

  def test_update_image(self):
    self.image.save_image()
    self.image.update_image_name(self.image.id,"name")
    update=Images.objects.get(name="name")
    self.assertEqual(update.name,"name")

  def test_search_category(self):
    self.location = Location(name='Nairobi')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)
    self.image.save_image()
    images=Images.search_image(self.category.id)
    self.assertTrue(len(images)==1)

  def test_filter_location(self):
    self.location = Location(name='nairobi')
    self.location.save_location()
    self.category = Category(name='tech')
    self.category.save_category()
    self.image=Images(id=1,image="image.png",name='laptop',description='new laptop',location=self.location,category=self.category)
    self.image.save_image()
    images = Images.filter_by_location("nairobi")
    self.assertTrue(len(images) > 0)

  def test_get_image_by_id(self):
    self.location = Location(name='nairobi')
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

  def test_category_instance(self):
    self.assertTrue(isinstance(self.tech,Category))
    self.assertTrue(isinstance(self.food,Category))
    self.assertTrue(isinstance(self.fitness,Category))

  def tearDown(self):
    Category.objects.all().delete()

  def test_save_category(self):
    self.food.save_category()
    self.fitness.save_category()
    self.tech.save_category()
    category=Category.objects.all()
    self.assertEqual(len(category),3)

  def test_delete_category(self):
    self.tech.save_category()
    self.fitness.save_category()
    self.fitness.delete_category()
    category=Category.objects.all()
    self.assertTrue(len(category)==1)

  def test_update_category(self):
    self.tech.save_category()
    self.tech.update_category(self.tech.id,'technology')
    update=Category.objects.get(name='technology')
    self.assertTrue(update.name,'technology')

class LocationTest(TestCase):
  def setUp(self):
    self.nairobi=Location(name='Nairobi')
    self.chicago=Location(name='Chicago')

  def test_location_instance(self):
    self.assertTrue(isinstance(self.nairobi, Location))
    self.assertTrue(isinstance(self.chicago, Location))

  def test_save_location(self):
    self.chicago.save_location()
    self.nairobi.save_location()
    location = Location.objects.all()
    self.assertTrue(len(location),2) 

  def tearDown(self):
    Location.objects.all().delete()

  def test_delete_location(self):
    self.chicago.save_location()
    self.nairobi.save_location()
    self.nairobi.delete_location()
    location=Location.objects.all()
    self.assertTrue(len(location)==1)

  def test_update_location(self):
    self.nairobi.save_location()
    self.nairobi.update_location(self.nairobi.id,'Ngong')
    update=Location.objects.get(name='Ngong')
    self.assertEqual(update.name,'Ngong')