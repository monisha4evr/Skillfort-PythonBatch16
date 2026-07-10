from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from .models import StudentDetails

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
        #print(request.POST.get('student_name'))
        student_name=request.POST.get('student_name')
        depart_name=request.POST.get('depart_name')
        addr=request.POST.get('address')
        course=request.POST.get('course')
        fees_paid=request.POST.get('fees_paid')

        sd=StudentDetails.objects.create(
            student_name=student_name,
            depart_name=depart_name,
            address=addr,
            course=course,
            fees_paid=fees_paid
        )
        print(sd);
        # return redirect("Student_details")
        stud_details=StudentDetails.objects.all()
        return render(request,"register.html",{"student_details":stud_details})
    return render(request,"register.html")

def update_student(request,id):
    sd=StudentDetails.objects.get(id=id)
    if request.method =="POST":
        sd.student_name=request.POST.get('student_name')
        sd.depart_name=request.POST.get('depart_name')
        sd.address=request.POST.get('address')
        sd.course=request.POST.get('course')
        sd.fees_paid=request.POST.get('fees_paid')
        sd.save()
        return redirect ("Student_details")
    return render(request,"update.html")