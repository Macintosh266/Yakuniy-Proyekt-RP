import re
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

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_admin') is not True:
            return ValueError("Sizda is_admin==True b'olishi kerak")
        if extra_fields.get('is_active') is not True:
            return ValueError()

        return  self.create_user(username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    phone=models.CharField(max_length=13,unique=True)
    email = models.CharField(max_length=50, null=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS = []




    def __str__(self):
        return self.phone

    @property
    def is_superuser(self):
        return self.is_admin

    def clean(self):
        super().clean()
        if self.phone and not re.match(r'^\+?\d{9,15}$', self.phone):
            raise ValidationError({'phone': 'Telefon raqami noto‘g‘ri formatda. Masalan: +998901234567'})


