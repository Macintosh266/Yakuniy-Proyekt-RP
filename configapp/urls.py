from os.path import basename
from django.urls import path,include
from rest_framework.routers import Route, DefaultRouter
from .views import *
from .views.HomeworkView import GiveHomework
from .views.StaffView import ManagerOrganizationView

router=DefaultRouter()
router.register(r'Student',StudentView,basename='studentcrud')
router.register(r'Group', CrudGroupView, basename='group-create')
router.register(r'Teacher',TeacherView,basename='teachercrud')
router.register(r'News',NewsViews,basename='newscrud')
router.register(r'Staff',ManagerOrganizationView,basename='stafff')
router.register(r'Table',CrudTableView,basename='table')
router.register(r'AttandanceLevel',AttendanceLevelView,basename='attendace_level')



urlpatterns=[
    path('', include(router.urls)),
    path('attendance/<int:group>/',AttendanceGroupView.as_view(),name='attendancegroup'),
    path('mock/<str:date1>/<str:date2>/data/',DataMock.as_view(),name='datamock'),
    path('mock/<str:year>/student/',StudentMonthMock.as_view(),name='stdmock'),
    path('mock/<str:date1>/<str:date2>/',SecondDataMock.as_view(),name='seconddatamock'),
    path('homework/<int:hw>/do/',DoHomework.as_view(),name='do_homework'),
    path('homework/<int:group>/give/',GiveHomework.as_view(),name='give_homework'),
    path('homework/<int:group>/check/',CheckHomework.as_view(),name='give_homework'),
    path('is_started/<int:pk>/lesson',TeacherCheckLesson.as_view(),name='check_lesson'),
    path('check/<int:pk>/group/',CheckGroup.as_view(),name='check_group'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/student/', StudentRegister.as_view(), name='register_student'),
    path('change/password/', ChangePassword.as_view(), name='change_password'),
    path('register/teacher/',RegisterTeacher.as_view(),name='register_teacher'),
    path('code/send/', SendEmailView.as_view(), name='send_code'),
    path('code/chack/',ChackEmailView.as_view(),name='check_code'),
]
