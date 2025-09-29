from django.db import models
from .auth_user import *
from .studentsmodel import *
from .teachersmodel import * 

class Days(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.title

class TableType(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.title

class Rooms(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        return self.title


class Table(models.Model):
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.ForeignKey(Rooms, on_delete=models.RESTRICT,related_name='room')
    type=models.ForeignKey(TableType, on_delete=models.RESTRICT,related_name='type')
    description=models.CharField(max_length=300,blank=True,null=True)




class Group(models.Model):
    title=models.CharField(max_length=50)
    course=models.ForeignKey(Course, related_name='get_course',on_delete=models.RESTRICT)
    teacher = models.ManyToManyField(Teacher, related_name='get_teacher')
    table=models.ForeignKey(Table,on_delete=models.RESTRICT,related_name='get_table')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    start_date=models.DateField()
    end_date=models.DateField()
    is_active=models.BooleanField(default=True)
    discription=models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        return self.title