from django.urls import path,include
from rest_framework.routers import Route, DefaultRouter
from .views import *
from .views.StaffView import ManagerOrganizationView

router=DefaultRouter()
router.register(r'Student',StudentView)
router.register(r'Group', CrudGroupView, basename='group-create')
router.register(r'Teacher',TeacherView)
router.register(r'News',NewsViews)
router.register(r'NewsPhoto',NewsPhotoViews)
router.register(r'Staff',ManagerOrganizationView)



urlpatterns=[
    path('./', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/student/', StudentRegister.as_view(), name='register_student'),
    path('change/password/', StudentChangePassword.as_view(), name='change_password'),
    path('register/teacher/',RegisterTeacher.as_view(),name='register_teacher'),
    path('code/send/', SendEmailView.as_view(), name='send_code'),
    path('code/chack/',ChackEmailView.as_view(),name='check_code'),
]