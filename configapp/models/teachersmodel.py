from django.db import models
from  .auth_user import *


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name