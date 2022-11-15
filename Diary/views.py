from django.shortcuts import render, redirect
from .forms import JournalForm, DiaryRegister
from .models import Journal
from django.contrib import messages

# Create your views here.
def register_user(request):
    form = DiaryRegister()
    if request.method == "POST":
        form = DiaryRegister(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            messages.success(request, f"User '{uname}' created")
            form.save()
            return redirect("diary-home")
    return render(request, "diary/register.html", context={"form": form})

def home(request):
    journals = Journal.objects.all()
    return render(request, "diary/home.html", context={"journals": journals})


def create_diary(request):
    #create an instance of the form
    form = JournalForm()
    if request.method == "POST": 
        #if request is a post bind data to the form
        form = JournalForm(request.POST)
        #check if data in the form is valid
        if form.is_valid():
            #save the form
            messages.success(request, "Diary saved")
            form.save()
            return redirect("home")

    return render (request, "diary/create.html", context={"form": form})


#update and edit diary
def edits(request, id):
    #retrieve the data instance from the database
    diary = Journal.objects.get(id=id)

    #display the retrived data instance in the form
    form = JournalForm(instance=diary)

    if request.method == "POST":
        #on a post request, populate the instance of the database with the data
        form = JournalForm(request.POST, instance=diary)
        if form.is_valid():
            #if the form's fields are valid, save the form data
            messages.success(request, "Diary saved")
            form.save()
            return redirect("diary-home") #redirect to home url

    return render(request, "diary/edit.html", context={"form":form})


#read a diary
def read(request, id):
    #get the instance of the data from the model
    journal = Journal.objects.get(id=id)
    #display the instance using the template context
    return render(request, "diary/read.html", context={"journal": journal})


#delete a diary
def dele(request, id):
    #get the instance of the data from the model
    diary = Journal.objects.get(id=id)
    #check for response
    if request.method == "POST":
        diary.delete()
        messages.success(request, "Diary deleted")
        #on a post request, delete the data from the database
        #and redirect to  the home url
        return redirect("home")
    return render(request, "diary/del.html", context={"diary": diary} )



