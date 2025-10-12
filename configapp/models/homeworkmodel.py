from django.db import models
from ..models import *
from django.core.validators import MinValueValidator, MaxValueValidator


class Homework(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()  # Vazifaning matni yoki tafsiloti
    due_date = models.DateField()  # Topshirish muddati
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HomeworkGet(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='homework_submissions')
    ball = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    is_submitted = models.BooleanField(default=False)
    submission_file = models.FileField(upload_to='homework_submissions/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.student.full_name} - {self.homework.title}"