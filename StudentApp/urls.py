from django.contrib import admin
from django.urls import path,include
from .views import*

urlpatterns=[
    path('Student_Dashboard',Student_Dashboard,name='Student_Dashboard'),
    path('Student_attendence',Student_attendence,name='Student_attendence'),
    path('student_library',student_library,name='student_library'),
    path('student_layout',Student_Layout,name='student_layout')
]