from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact),
    path('about/',views.about),
    path('register/',views.student_details),
]
