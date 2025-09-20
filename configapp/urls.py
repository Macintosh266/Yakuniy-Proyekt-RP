from django.urls import path,include
from configapp.views.Crud_Teacher import *
from rest_framework.routers import Route, DefaultRouter
from configapp.views.Crud_Student import *
from configapp.views.SendEmail import *

router=DefaultRouter()
router.register(r'Student',StudentView)
# router.register(r'Teacher', TeacherView, basename='students-create')


urlpatterns=[
    # path('', include(router.urls)),
    path('crud/teacher/', TeacherView.as_view(), name='teacher_list_create'),
    path('crud/teacher/<int:pk>/', TeacherView.as_view(), name='teacher_detail'),
    # path('crud/student/', StudentView.as_view(), name='student_list_create'),
    # path('crud/student/<int:pk>/', StudentView.as_view(), name='student_detail'),
    path('send/email', SendEmailView.as_view(), name='send_email')
]