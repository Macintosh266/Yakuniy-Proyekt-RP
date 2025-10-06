from os.path import basename

from django.urls import path,include
from rest_framework.routers import Route, DefaultRouter
from .views import *
from .views.StaffView import ManagerOrganizationView

router=DefaultRouter()
router.register(r'Student',StudentView,basename='studentcrud')
router.register(r'Group', CrudGroupView, basename='group-create')
router.register(r'Teacher',TeacherView,basename='teachercrud')
router.register(r'News',NewsViews,basename='newscrud')
router.register(r'NewsPhoto',NewsPhotoViews,basename='newsphotocrud')
router.register(r'Staff',ManagerOrganizationView,basename='stafff')
router.register(r'Attendance',AttendanceView,basename='attendance-view')



urlpatterns=[
    path('', include(router.urls)),
    path('is_started/<int:pk>/lesson',TeacherCheckLesson.as_view(),name='check_lesson'),
    path('attendance/<int:pk>/level',AttendanceLevelView.as_view(),name='attendance_level'),
    path('check/<int:pk>/group/',CheckGroup.as_view(),name='check_group'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/student/', StudentRegister.as_view(), name='register_student'),
    path('change/password/', StudentChangePassword.as_view(), name='change_password'),
    path('register/teacher/',RegisterTeacher.as_view(),name='register_teacher'),
    path('code/send/', SendEmailView.as_view(), name='send_code'),
    path('code/chack/',ChackEmailView.as_view(),name='check_code'),
]