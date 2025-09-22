from django.db import models
from .auth_user import *
from .groupsmodel import Group



class Students(models.Model):
    full_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='get_group')
    discription=models.CharField(max_length=500,blank=True,null=True)
    is_line=models.BooleanField(default=False)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    

class Parent(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    student=models.ForeignKey(Students,on_delete=models.CASCADE,related_name='get_student')
    address=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    discription=models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.name

