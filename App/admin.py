from django.contrib import admin
from App.models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(LabTeacher)
admin.site.register(LabAttendent)
admin.site.register(Complains)
admin.site.register(Notice)
admin.site.register(LabInf)
admin.site.register(LabSchedule)