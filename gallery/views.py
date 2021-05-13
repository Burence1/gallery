from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Images
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
  images = Images.get_images()
  location = Location.objects.all()
  category= Category.objects.all()

  return render(request, 'index.html',{"images":images,"location":location,"category":category})

def search_images(request):
  if 'category' in request.GET and request.GET["category"]:
    search_term=request.GET.get("category")
    try:
      category=Category.objects.get(name=search_term)
      image=Images.search_image(category)
      message=f"found {len(image)}"
      return render(request,'search.html',{"message":message,"image":image})
    
    except ObjectDoesNotExist:
      message="O images found"
      categories= Category.objects.all()
      return render(request,"search.html",{"message":message,"categories":categories})

  else:
    message="Search for categories"
    return render(request,"search.html",{"message":message})

def category(request,category_id):
  try:
    category =Category.objects.get(id=category_id)
    images=Images.save_image(category)
    message=category.name
    title=category.name
    return render(request,'search.html',{"images":images,"message":message,"title":title})

  except ObjectDoesNotExist:
    message="This category has no images"
    categories=Category.objects.all()
    return render(request,'search.html',{"message":message,"categories":categories})

def single_image(request,image_id):
  try:
    image=Images.objects.get(id=image_id)
    return render(request,"image.html",{"image":image})

  except ObjectDoesNotExist:
    message="image does not exist"
    return (request,'image.html',{"message":message})

def location(request,location_id):
  try:
    location=Location.objects.get(id=location_id)
    images=Images.filter_by_location(location)
    message=location.name
    title=location.name
    return render(request,"search.html",{"images":images,"message":message,"title":title})
  
  except ObjectDoesNotExist:
    message="no image(s) in this location"
    location=Location.objects.all()
    title="No images"
    return render(request,"search.html",{"message":message,"location":location,"title":title})