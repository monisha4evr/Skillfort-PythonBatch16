from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact ,name="contact"),
    path('about/',views.about,name="about"),
    path('register/',views.student_details,name="Student_details"),
    path('update/<int:id>',views.update_student,name="update_student")
]
