from django.contrib import admin
from configapp.models.studentsmodel import *
from configapp.models.groupsmodel import *
from configapp.models.teachersmodel import *
from configapp.models.auth_user import *

admin.site.register([Students,Parent,TimePassword])
admin.site.register([Table,TableType,Rooms,Group,Days])
admin.site.register([Teacher,Departmenrt,Course])
admin.site.register([User])
# Register your models here.
