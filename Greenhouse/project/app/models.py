from django.db import models

# Create your models here.
class Student_details(models.Model):
    student_name=models.CharField(max_length=30),
    depart_name=models.CharField(max_length=50),

