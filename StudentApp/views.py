from django.shortcuts import render,redirect
from AdminApp.models import *
from TeacherApp.models import Study_Material
# Create your views here.
def Student_Dashboard(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            ni=Notifications.objects.all()
            student=Students.objects.get(student_email=user_id)
            return render(Http_req,'Student_Dashboard.html',{'user_id':user_id,'student':student,'ni':ni})
    except KeyError:
        return redirect('loginpage')
def Student_attendence(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            ni=Notifications.objects.all()
            student=Students.objects.get(student_email=user_id)
            att=Attendence.objects.filter(student_attendence_id=student.student_enrollment_id)
            return render(Http_req,'student_attendence.html',{'user_id':user_id,'att':att,'ni':ni})
    except KeyError:
        return redirect('loginpage')
def student_library(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            ni=Notifications.objects.all()
            student=Students.objects.get(student_email=user_id)
            slm=Study_Material.objects.filter(Document_for_class=student.student_class)
            return render(Http_req,'student_library.html',{'user_id':user_id,'student':student,'slm':slm,'ni':ni})
    except KeyError:
        return redirect('loginpage')
def Student_Layout(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            ni=Notifications.objects.all()
            student=Students.objects.get(student_email=user_id)
            return render(Http_req,'Student_Layout.html',{'user_id':user_id,'student':student,'ni':ni})
    except KeyError:
        return redirect('loginpage')