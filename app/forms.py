from .models import Task
from django import forms 

class Add_form(forms.ModelForm):
    class Meta:
        model = Task 
        fields = '__all__'