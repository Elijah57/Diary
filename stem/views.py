from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.template import loader
from .models import Posts

# Create your views here.
# posts = [
#     {
#         "author": "Elijah Echekwu",
#         "title" : "DC- Motors",
#         "content": "DC motors are motores that are powered with direct current/voltages",
#         "date_posted":"September 29, 2022"
#     },
#     {
#         "author": "Elijah Echekwu",
#         "title" : "AC- Motors",
#         "content": "AC motors are motores that are powered with alternating current/voltages",
#         "date_posted":"September 30, 2022"
#     }

# ]

def home(request):
    posts = Posts.objects.all()
    context={"posts": posts}
    return render(request, "stem/home.html", context)




def curriculum(request):
    return render(request, "stem/index.html")


def info(request):
    return render(request, "stem/about.html")

