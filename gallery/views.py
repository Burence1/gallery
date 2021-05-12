from django.shortcuts import render
from .models import Location,Category,Images
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
  images = Images.get_images()
  location = Location.objects.all()
  category= Category.objects.all()

  return render(request, 'index.html',{"images":images,"location":location,"category":category})