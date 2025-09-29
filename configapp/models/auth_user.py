import random
import re
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self,phone,password=None,**extra_fields):
        if not phone:
            return  ValueError('User kiritish shart!')
        user=self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)

        if extra_fields.get('is_admin') is not True:
            return ValueError("Sizda is_admin==True b'olishi kerak")
        if extra_fields.get('is_active') is not True:
            return ValueError("Siz activ emasiz")
        if extra_fields.get('is_staff') is not True:
            return ValueError("Sizda is_staff==True b'olishi kerak")

        return  self.create_user(phone,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=13,unique=True)
    email = models.CharField(max_length=50, unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS = ['email']




    def __str__(self):
        return self.phone

    @property
    def is_superuser(self):
        return self.is_admin

    def clean(self):
        super().clean()
        if self.phone and not re.match(r'^\+?\d{9,15}$', self.phone):
            raise ValidationError({'phone': 'Telefon raqami noto‘g‘ri formatda. Masalan: +998901234567'})



class TimePassword(models.Model):
    email=models.EmailField()
    time_password = models.CharField(max_length=5)
    is_bool = models.BooleanField(default=False)
    code_created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.is_bool}"


    def set_reset_code(self):
        code = str(random.randint(10000, 99999))
        self.time_password = code
        self.save()
        return code

    def is_code_valid(self, code):
        if self.time_password != code:
            return False
        if not self.code_created_at:
            return False
        elapsed = timezone.now() - self.code_created_at
        return elapsed.total_seconds() <= 300

