from django.db import models
from .auth_user import *
from .groupsmodel import Group
from django.utils import timezone
from datetime import timedelta


class Students(models.Model):
    full_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='get_group')
    discription=models.CharField(max_length=500,blank=True,null=True)
    is_line=models.BooleanField(default=False)
    is_finish=models.BooleanField(default=False)
    address=models.CharField(max_length=50)
    category=models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.is_line and not self.is_line_set_at:
            self.is_line_set_at = timezone.now()

        if not self.is_line:
            self.is_line_set_at = None

        super().save(*args, **kwargs)

    def is_line_valid(self):
        """is_line True bo‘lib 12 soatdan oshgan bo‘lsa, False qaytaradi"""
        if not self.is_line or not self.is_line_set_at:
            return False
        return timezone.now() - self.is_line_set_at < timedelta(hours=12)


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


