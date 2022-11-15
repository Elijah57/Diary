from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users

# Create your views here.

#create a request handler, 
# #so that when a request is made the function handles the request
#we can pull data from database
#send email
def home(request):
    return HttpResponse("hello")

def tell_info(request):
    return render(request, "playground/info.html")   

def About(request):
    return render(request, "playground/hello.html", {"name": "Elijah"}) 

def Register(request):
    return render(request, "playground/register.html")

def add_to_db(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    sex = request.POST["sex"]
    mail_address = request.POST["mail"]
    date = request.POST["create"]
    pj_name = request.POST["project_name"]
    description = request.POST["description"]
    user = Users(firstname=fname, lastname=lname, email=mail_address,
    sex=sex, created_at=date, description=description, project_name=pj_name)
    user.save()
    return HttpResponseRedirect(reverse("home"))
    
