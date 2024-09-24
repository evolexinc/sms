from django.shortcuts import *
from AdminApp.models import Teachers, Attendence, Students,Notifications
from django.core.files.storage import FileSystemStorage
from .models import Study_Material
import datetime


# Create your views here.
# teacher Dashboard
def Teacher_Dashboard(Http_req):
    user_id = Http_req.session["user_id"]
    try:
        if user_id != None:
            return render(Http_req, "Teacher_Dashboard.html", {"user_id": user_id})
    except KeyError:
        return redirect("loginpage")


# profile
def Teacher_profile(Http_req):
    user_id = Http_req.session["user_id"]
    teacher = Teachers.objects.get(teacher_id=user_id)
    try:
        if user_id != None:
            return render(Http_req, "Teacher_profile.html", {"teacher": teacher})
    except KeyError:
        return redirect("loginpage")


def uploadpic(req):
    if req.method == "POST":
        teacherid = req.session["user_id"]
        teacher = Teachers.objects.get(teacher_id=teacherid)
        teacher_profile_image = req.FILES["pic"]
        fs = FileSystemStorage()
        filename = fs.save(teacher_profile_image.name, teacher_profile_image)
        teacher.teacher_profile_image = filename
        teacher.save()
        return redirect("TeacherApp:Teacher_Profile")


# attendence
def Student_Attendence(Http_req):
    user_id = Http_req.session["user_id"]
    try:
        if user_id != None:
            teacher = Teachers.objects.get(teacher_id=user_id)
            stu = Students.objects.filter(student_class=teacher.teacher_allocated_classes)
            attend = Attendence.objects.filter(student_attendence_id=teacher.teacher_id)
            if Http_req.method == "POST":
                student_attendence_enrollment_id = Http_req.POST[
                    "student_attendence_enrollment_id"
                ]
                student_attendence_name = Http_req.POST["student_attendence_name"]
                student_attendence_id = Http_req.POST["student_attendence_id"]
                student_attendence_status = Http_req.POST["student_attendence_status"]
                student_attendence_date = Http_req.POST["student_attendence_date"]
                
                a=Attendence.objects.filter(student_attendence_enrollment_id=student_attendence_enrollment_id,student_attendence_date=student_attendence_date).first()
                if a is not None:
                    msg='Already marked Attendence for this Student '
                    return render( Http_req, "Student_Attendence.html", {"user_id": user_id, "stu": stu,'attend':attend,'msg':msg})
                
                
                else:
                    att = Attendence(
                    student_attendence_enrollment_id=student_attendence_enrollment_id,
                    student_attendence_name=student_attendence_name,
                    student_attendence_id=student_attendence_id,
                    student_attendence_status=student_attendence_status,
                    student_attendence_date=student_attendence_date,
                )
                    att.save()
                    return redirect("TeacherApp:Student_Attendence")
            return render(
                Http_req, "Student_Attendence.html", {"user_id": user_id, "stu": stu,'attend':attend}
            )
    except KeyError:
        return redirect("loginpage")


# Announcements
def Teacher_Announcements(Http_req):
    user_id = Http_req.session["user_id"]
    try:
        if user_id != None:
            ni=Notifications.objects.all()
            return render(Http_req, "Teacher_Announcements.html", {"user_id": user_id,'ni':ni})
    except KeyError:
        return redirect("loginpage")


# Password
def Teacher_Password(req):
    user_id = req.session["user_id"]
    # try:
    if user_id != None:
        teacher = Teachers.objects.get(teacher_id=user_id)
        if req.method == "POST":
            oldPassword = req.POST["oldPassword"]
            newPassword = req.POST["newPassword"]
            cnfPassword = req.POST["cnfPassword"]
            if newPassword != cnfPassword:
                msg = "Please Enter same Password"
                return render(req, "Teacher_Password.html", {"msg": msg})
            elif teacher.teacher_password != oldPassword:
                msg = "wrong Password"
                return render(req, "Teacher_Password.html", {"msg": msg})
            elif teacher.teacher_password == oldPassword:
                Teachers.objects.filter(teacher_id=user_id).update(
                    teacher_password=newPassword
                )
                return redirect("TeacherApp:Teacher_Dashboard")
        return render(req, "Teacher_Password.html", {"teacher": teacher})
    # except KeyError:
    # return redirect('loginpage')


# SLM
def Teacher_SLM(Http_req):
    user_id = Http_req.session["user_id"]
    try:
        if user_id != None:
            teacher = Teachers.objects.get(teacher_id=user_id)
            if Http_req.method=="POST":

                Document_title=Http_req.POST['Document_title']
                Document_location=Http_req.FILES['Document_location']
                sl=Study_Material(Document_title=Document_title,Document_location=Document_location,Document_for_class=teacher.teacher_allocated_classes)
                sl.save()
                return redirect('TeacherApp:Teacher_SLM')
            stl=Study_Material.objects.all()
            return render(Http_req, "Teacher_SLM.html", {"user_id": user_id,'teacher':teacher,'stl':stl})
    except KeyError:
        return redirect("loginpage")


def tchange_password(req):
    try:
        if req.session["user_id"] != None:
            user_id = req.session["user_id"]
            teacher = Teachers.objects.get(treacher_id=user_id)
            if req.method == "POST":
                oldpassword = req.POST["oldpassword"]
                newpassword = req.POST["newpassword"]
                cnfpassword = req.POST["cnfpassword"]
                if newpassword != cnfpassword:
                    msg = "Please Enter same Password"
                    return render(req, "Teacher_Password.html", {"msg": msg})
                elif teacher.teacher_password != oldpassword:
                    msg = "wrong Password"
                    return render(req, "Teacher_Password.html", {"msg": msg})
                elif teacher.teacher_password == oldpassword:
                    Teachers.objects.filter(teacher_id=user_id).update(
                        teacher_password=newpassword
                    )
                    return redirect("TeacherApp:Teacher_Dashboard")
            return render(req, "Teacher_Password.html", {"teacher": teacher})
    except KeyError:
        return redirect("login")
