from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("This is my home page")

    context = {"name":"Arnab","age": 19,"course":"django"}
    return render(request,"index.html",context)

def about(request):
    # return HttpResponse("This is my about page")
    return render(request,"about.html")

def contact(request):
    # return HttpResponse("This is my contact page")
    return render(request,"contact.html")

def projects(request):
    # return HttpResponse("This is my prjects page")
    return render(request,"projects.html")

