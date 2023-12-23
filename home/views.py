from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is my home page")

def about(request):
    return HttpResponse("This is my about page")

def contact(request):
    return HttpResponse("This is my contact page")

def projects(request):
    return HttpResponse("This is my prjects page")

