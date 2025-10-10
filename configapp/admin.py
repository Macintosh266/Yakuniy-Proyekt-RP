from django.contrib import admin
from .models import *

admin.site.register([Students,Parent,TimePassword])
admin.site.register([Table,TableType,Rooms,Group,Days])
admin.site.register([Teacher,Departmenrt,Course])
admin.site.register([User])
admin.site.register([Homework])
admin.site.register([Attendance,AttendanceLevel])
admin.site.register([About])
admin.site.register([News,NewsFotos])
admin.site.register([ManagerOrganization,Organization,Region])



# Register your models here.
