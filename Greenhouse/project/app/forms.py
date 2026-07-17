from django.forms import ModelForm
from .models import StudentDetails 
from django import forms

class StudentForm(ModelForm):
    price = forms.IntegerField(required=True)
    class Meta:
        model = StudentDetails
        fields = "__all__"
        #fields = ['name','address','course]

