from django.urls import path
from .views import *
urlpatterns=[
    path('Teacher_Dashboard',Teacher_Dashboard,name='Teacher_Dashboard'),
    path('Teacher_Profile',Teacher_profile,name='Teacher_Profile'),
    path('Student_Attendence',Student_Attendence,name='Student_Attendence'),
    path('Teacher_Announcements',Teacher_Announcements,name='Teacher_Announcements'),
    path('Teacher_Password',Teacher_Password,name='Teacher_Password'),
    path('Teacher_SLM',Teacher_SLM,name='Teacher_SLM'),
    path('uploadpic/',uploadpic,name='uploadpic'),
  
]