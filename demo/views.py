from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def staticpage(request):
    return HttpResponse('static page')

def dynamicpage(request,st):
    return HttpResponse('Moshi Moshi '+st)

