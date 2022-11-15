from django.forms import ModelForm
from django import forms
from .models import Journal
from django.forms.widgets import DateTimeBaseInput
import datetime
from django.contrib.admin import widgets
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class JournalForm(ModelForm):
    #date = forms.DateTimeField(widget=DateTimeBaseInput())
    
    class Meta:
        model = Journal
        fields = ["date", "mood", "title", "story"]

        widgets = {
            "date" : DateTimePickerInput(format='%Y-%m-%d %H:%M:%S')
                 
        }
    

class DiaryRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
