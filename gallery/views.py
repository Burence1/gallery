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
      message=f"found {{images|length}}"
      return render(request,'search.html',{"message":message,"image":image})
    
    except ObjectDoesNotExist:
      message="O images found"
      categories= Category.objects.all()
      return render(request,"search.html",{"message":message,"categories":categories})

  else:
    message="Search for categories"
    return render(request,"search.html",{"message":message})