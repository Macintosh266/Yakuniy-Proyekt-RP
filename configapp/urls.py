from django.urls import path,include
from configapp.views.Crud_Teacher import *
from rest_framework.routers import Route, DefaultRouter
from configapp.views.Crud_Student import *
from configapp.views.SendEmail import *
from configapp.views.GroupView import *
from configapp.views.Login_View import *

router=DefaultRouter()
router.register(r'Student',StudentView)
router.register(r'Group', CrudGroupView, basename='group-create')


urlpatterns=[
    path('./', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/student/', StudentRegister.as_view(), name='register_student'),
    path('change/password/', StudentChangePassword.as_view(), name='change_password'),
    path('register/teacher/',RegisterTeacher.as_view(),name='register_teacher'),
    path('teacher/crud/', TeacherView.as_view(), name='teacher_list_create'),
    path('teacher/<int:pk>/crud/', TeacherView.as_view(), name='teacher_detail'),
    path('code/send/', SendEmailView.as_view(), name='send_code'),
    path('code/chack/',ChackEmailView.as_view(),name='check_code'),
]