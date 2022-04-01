from django.shortcuts import render,redirect
from .models import Video


def objects_all(object):
  objects = object.objects.all()
  return objects

def objects_get(object , pk = None , slug = None):
  if pk != None:
    objects = object.objects.get(pk=pk)
    return objects
  elif slug != None:
    objects = object.objects.get(slug=slug)
    return objects


def index(request):
    return render(request, 'base.html')

def home_page(request):
  video = objects_all(Video)
  return render(request , 'home_page.html' , {'video' : video,})

def product_detail(request):
    video = objects_get(Video, slug=slug)
    return render(request, 'product_detail.html', {'video': video, 'form': form})