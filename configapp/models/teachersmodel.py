from django.db import models
from  .auth_user import *

class Departmenrt(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=300,blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=300,blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name=models.CharField(max_length=50)
    departament=models.ManyToManyField(Departmenrt,related_name='get_departament')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discription=models.CharField(max_length=500,blank=True,null=True)
    course=models.ManyToManyField(Course,related_name='course')

    def __str__(self):
        return self.full_name