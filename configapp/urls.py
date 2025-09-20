from django.urls import path,include
from configapp.views.Crud_Teacher import *
from rest_framework.routers import Route, DefaultRouter
from configapp.views.Crud_Student import *
from configapp.views.SendEmail import *
from configapp.views.GroupView import *

router=DefaultRouter()
router.register(r'Student',StudentView)
router.register(r'Group', CrudGroupView, basename='group-create')


urlpatterns=[
    # path('', include(router.urls)),
    path('crud/teacher/', TeacherView.as_view(), name='teacher_list_create'),
    path('crud/teacher/<int:pk>/', TeacherView.as_view(), name='teacher_detail'),
    # path('crud/student/', StudentView.as_view(), name='student_list_create'),
    # path('crud/student/<int:pk>/', StudentView.as_view(), name='student_detail'),
    path('send/code', SendEmailView.as_view(), name='send_code'),
    path('chack/code',ChackEmailView.as_view(),name='check_code'),
]