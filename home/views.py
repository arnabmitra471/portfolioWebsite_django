from django.shortcuts import render
from home.models import Contact
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
    if request.method == "POST":
        name = request.POST["fname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        concern = request.POST["concern"]
        # print(name,phone,email,concern)
        info = Contact(name=name,phone=phone,email=email,concern=concern)
        info.save()
        print("The data has been written to the db")
    return render(request,"contact.html")

def projects(request):
    # return HttpResponse("This is my prjects page")
    return render(request,"projects.html")

