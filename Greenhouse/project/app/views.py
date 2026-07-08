from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Student_details

# Create your views here.
def home(request):
    return render (request,"home.html")

def contact(request):
    return HttpResponse("Hello world")

def about(request):
    info={
        'category':"fruit",
        "name":"apple",
        "city":['Kashmir','Tamilnadu'],
        "price":105,
        "received_at":date(2026,7,10)
    }
    return render(request,"about.html",info)

def student_details(request):
    if request.method=="POST":
        pass

    var=Student_details.objects.all()
    return render(request,"register.html")