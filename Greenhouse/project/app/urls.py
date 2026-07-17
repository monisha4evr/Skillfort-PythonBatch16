from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import TemplateExampleView

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact ,name="contact"),
    path('about/',views.about,name="about"),
    path('register/',views.student_details,name="Student_details"),
    path('update/<int:id>',views.update_student,name="update_student"),
    path('delete/<int:id>',views.delete_student,name="delete_student"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.signout,name="signout"),
    path('style/',views.styleexample),
    path('student_form/',views.student_form,name="student_form"),
    path('student-filter/',views.student_filter,name="student_filter"),
    path('template-home/',TemplateView.as_view(template_name="templatehome.html",extra_context={"name":"Apple","color":"red"}),name="template_home"),
    path('template-examp/', TemplateExampleView.as_view(), name="template_example"),
]
