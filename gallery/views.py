from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Images
from django.core.exceptions import ObjectDoesNotExist
import numpy as num
import pyperclip

# Create your views here.
def index(request):
  images = Images.get_images()
  new = num.array(images)
  split_arr = num.array_split(new, 3)
  first = split_arr[0]
  second = split_arr[1]
  third = split_arr[2]
  location = Location.objects.all()
  category= Category.objects.all()

  return render(request, 'index.html', {"first": first, "second": second, "third": third, "location": location, "category": category})

def search_images(request):
  if 'category' in request.GET and request.GET["category"]:
    search_term=request.GET.get("category")
    try:
      category=Category.objects.get(name=search_term)
      image=Images.search_image(category)
      new = num.array(image)
      split_arr = num.array_split(new, 3)
      first = split_arr[0]
      second = split_arr[1]
      third = split_arr[2]
      message=f"found {len(image)}"
      return render(request, 'search.html', {"message": message, "image": image, "first": first, "second": second, "third": third })
    
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
    image=Images.search_image(category)
    new = num.array(image)
    split_arr = num.array_split(new, 3)
    first = split_arr[0]
    second = split_arr[1]
    third = split_arr[2]
    message=category.name
    title=category.name
    return render(request, 'search.html', {"image":image,"first": first, "second": second, "third": third,"message": message, "title": title})

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
    image=Images.filter_by_location(location)
    new = num.array(image)
    split_arr = num.array_split(new, 3)
    first = split_arr[0]
    second = split_arr[1]
    third = split_arr[2]
    message=location.name
    title=location.name
    return render(request, "search.html", {"image":image,"first": first, "second": second, "third": third,"message": message, "title": title})
  
  except ObjectDoesNotExist:
    message="no image(s) in this location"
    location=Location.objects.all()
    title="No images"
    return render(request,"search.html",{"message":message,"location":location,"title":title})
