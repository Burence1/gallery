from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Images
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
  images = Images.objects.all()
  location = Location.objects.all()
  category= Category.objects.all()

  return render(request, 'index.html',{"images":images,"location":location,"category":category})