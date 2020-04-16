from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task #name of model
        fields = '__all__' #all fields in the model