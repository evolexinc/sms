from django.urls import path
from django.contrib import admin
from .views import*

urlpatterns=[
    path('/Dashboard',Dashboard,name='Dashboard'),
    path('/view_enq',view_enq,name='view_enq'),
    path('/viewclasses',viewclasses,name="viewclasses"),
    path('/faculties',faculties,name='faculties'),
    path('/students',students,name='students'),
    path('/subjects',subjects,name='subjects'),
    path('/admin_logout',admin_logout,name='admin_logout'),
    path('/delete_enq/<id>',delete_enq,name='delete_enq'),
    path('/delete_teacher/<id>',delete_teacher,name='delete_teacher'),
    path('editclass/<id>',editclass,name="editclass"),
    path('/delete_student/<id>',delete_student,name='delete_student'),
    path('editsubjects/<id>',edit_subjects,name='edit_subjects'),
    path('editstudents/<id>',edit_students,name='edit_students'),
    path('/delete_class/<id>',delete_class,name='delete_class'),
    path('/delete_subject/<id>',delete_subject,name='delete_subject'),



]