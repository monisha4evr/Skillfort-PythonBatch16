from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student_name=models.CharField(max_length=30)
    depart_name=models.CharField(max_length=50)
    address=models.CharField( max_length=50,blank=True,default='')
    course=models.CharField(max_length=50,blank=True,default='')
    fees_paid=models.DecimalField( max_digits=5, decimal_places=2,null=True)

    def __str__(self):
        return self.student_name

