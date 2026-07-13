from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import StudentDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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
    if request.method == "POST":
        StudentDetails.objects.create(
            student_name=request.POST.get("student_name"),
            depart_name=request.POST.get("depart_name"),
            address=request.POST.get("address"),
            course=request.POST.get("course"),
            fees_paid=request.POST.get("fees_paid")
        )

        return redirect("Student_details")

    stud_details = StudentDetails.objects.all()

    return render(
        request,
        "register.html",
        {"student_details": stud_details}
    )

def update_student(request,id):
    sd = get_object_or_404(StudentDetails, id=id)
   # sd=StudentDetails.objects.get(id=id)
    if request.method =="POST":
        sd.student_name=request.POST.get('student_name')
        sd.depart_name=request.POST.get('depart_name')
        sd.address=request.POST.get('address')
        sd.course=request.POST.get('course')
        sd.fees_paid=request.POST.get('fees_paid')
        sd.save()
        return redirect ("Student_details")
    return render(request, "update.html", {"student": sd})

def delete_student(request,id):
    sd = get_object_or_404(StudentDetails, id=id) 
    sd.delete()
    return redirect('Student_details')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password != confirm_password:
             return render(request, "signup.html", {
                "error": "Password mismatch"
            })
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists"
            })
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email already registered"
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("signin")

    return render(request, "UserRegistration.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("home")

    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("signin")