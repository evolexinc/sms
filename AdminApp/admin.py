from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(classes)
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Attendence)
admin.site.register(Notifications)

