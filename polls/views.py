from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello. world , You're at the polls index")

def details(request, id):
    return HttpResponse(f" You are looking at question {id}")

def result(request, id):
    return HttpResponse(f"This is the result of the question {id}")

def vote(request, id):
    return HttpResponse(f"You're voting on this Question {id}")
