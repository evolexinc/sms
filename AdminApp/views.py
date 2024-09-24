from django.shortcuts import render,redirect
from SMSMyApp.models import *
from .models import *
from django.views.decorators.cache import cache_control
from django.utils import timezone
import datetime


# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def Dashboard(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            if Http_req.method == "POST":
                notification_msg=Http_req.POST['notification_msg']
                notification_document=Http_req.FILES['notification_document']
                notification_date=timezone.now()
                notification=Notifications(notification_msg=notification_msg,notification_document=notification_document,notification_date=notification_date)
                notification.save()
                
                return redirect('AdminApp:Dashboard')
            ni=Notifications.objects.all()
            student_count=Students.objects.all().count()
            teacher_count=Teachers.objects.all().count()
            subjects_count=Subjects.objects.all().count()
            class_count=classes.objects.all().count()
            ps=Attendence.objects.filter(student_attendence_status='P',student_attendence_date=datetime.date.today()).count()
            absent=Attendence.objects.filter(student_attendence_status='A',student_attendence_date=datetime.date.today()).count()
            
            return render(
                Http_req,
                'Dashboard.html',
                {'user_id':user_id,
                'student_count':student_count,
                'teacher_count':teacher_count,
                'class_count':class_count,
                'subject_count':subjects_count,
                'ps':ps,
                'absent':absent,
                'ni':ni

                })
    except KeyError:
        return redirect('loginpage')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def view_enq(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            enq=Enquiry.objects.all()
            ni=Notifications.objects.all()
            return render(Http_req,'view_enquiry.html',{'user_id':user_id,'enq':enq,'ni':ni})
    except KeyError:
        return redirect('loginpage')
    
'''view for classes.html'''
#View class
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewclasses(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            if Http_req.method=='POST':
                    class_name=Http_req.POST['class_name']
                    class_seats=Http_req.POST['class_seats']
                    class_location=Http_req.POST['class_location']
                    class_subjects=Http_req.POST['class_subjects']
                    class_teacher=Http_req.POST['class_teacher']
                    cl=classes(class_name=class_name,class_seats=class_seats,class_location=class_location,class_subjects=class_subjects,class_teacher=class_teacher)
                    cl.save()
                    return redirect('AdminApp:viewclasses')
            cls=classes.objects.all()
            ni=Notifications.objects.all()
            return render(Http_req,'viewclasses.html',{'user_id':user_id,'cls':cls,'ni':ni})
    except KeyError:
        return redirect('loginpage')

'''view for Faculties.html'''
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def faculties(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            if Http_req.method=="POST":
                teacher_name=Http_req.POST['teacher_name']
                teacher_father_name=Http_req.POST['teacher_father_name']
                teacher_mother_name=Http_req.POST['teacher_mother_name']
                teacher_gender=Http_req.POST['teacher_gender']
                teacher_dob=Http_req.POST['teacher_dob']
                teacher_phone=Http_req.POST['teacher_phone']
                teacher_email=Http_req.POST['teacher_email']
                teacher_password=Http_req.POST['teacher_password']
                teacher_allocated_classes=Http_req.POST['teacher_allocated_classes']
                teacher_address=Http_req.POST['teacher_address']
                teacher_salary=Http_req.POST['teacher_salary']
                teacher_qualification=Http_req.POST['teacher_qualification']
                teacher_profile_image=Http_req.POST['teacher_profile_image']
                teacher_joining_date=timezone.now()
                teacher=Teachers(
                    teacher_name=teacher_name,
                    teacher_father_name=teacher_father_name,
                    teacher_mother_name=teacher_mother_name,
                    teacher_gender=teacher_gender,
                    teacher_dob=teacher_dob,
                    teacher_phone=teacher_phone,
                    teacher_email=teacher_email,
                    teacher_password=teacher_password,
                    teacher_allocated_classes=teacher_allocated_classes,
                    teacher_address=teacher_address,
                    teacher_salary=teacher_salary,
                    teacher_qualification=teacher_qualification,
                    teacher_profile_image=teacher_profile_image,
                    teacher_joining_date=teacher_joining_date
                    )
                teacher.save()

                return redirect('AdminApp:faculties')
            cls=classes.objects.all()
            fc=Teachers.objects.all()
            return render(Http_req,'faculties.html',{'user_id':user_id,'cls':cls,'fc':fc})
    except KeyError:
        return redirect('loginpage')
''' deletion  of teacher '''
def delete_teacher(http_req,id):
    user_id=http_req.session['user_id']
    try:
        if user_id != None:
            Teachers.objects.get(teacher_id=id).delete()
            return redirect('AdminApp:faculties')
    except KeyError:
        return redirect('loginpage')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def students(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            cls=classes.objects.all()
            sts=Students.objects.all()
            if Http_req.method=="POST":
            
            
                student_adhar=Http_req.POST['student_adhar']
                student_name=Http_req.POST['student_name']
                student_father_name=Http_req.POST['student_father_name']
                student_mother_name=Http_req.POST['student_mother_name']
                student_gender=Http_req.POST['student_gender']
                student_dob=Http_req.POST['student_dob']
                student_phone=Http_req.POST['student_phone']
                student_parents_phone=Http_req.POST['student_parents_phone']
                student_email=Http_req.POST['student_email']
                student_class=Http_req.POST['student_class']
                student_address=Http_req.POST['student_address']
                student_fee=Http_req.POST['student_fee']
                student_subjects=Http_req.POST['student_subjects']
                student_profile_image=Http_req.POST['student_profile_image']
                student_admission_date=timezone.now()
                stu=Students.objects.filter(student_email=student_email).first()
                if stu is not None:
                    return render(Http_req,'students.html',{'user_id':user_id,'cls':cls,'sts':sts,'msg':'This Email Address is already Taken'})
                else:
                    student=Students(
                            student_adhar=student_adhar,
                            student_name=student_name,
                            student_father_name=student_father_name,
                            student_mother_name=student_mother_name,
                            student_gender=student_gender,
                            student_dob=student_dob,
                            student_phone=student_phone,
                            student_parents_phone=student_parents_phone,
                            student_email=student_email,
                            student_password="student@1234",
                            student_class=student_class,
                            student_address=student_address,
                            student_fee=student_fee,
                            student_subjects=student_subjects,
                            student_profile_image=student_profile_image,
                            student_admission_date=student_admission_date
                            )
                    student.save()
                    return redirect('AdminApp:students')
            
            return render(Http_req,'students.html',{'user_id':user_id,'cls':cls,'sts':sts})
    except KeyError:
         return redirect('loginpage')
''' deletion  of Students '''
def delete_student(http_req,id):
    user_id=http_req.session['user_id']
    try:
        if user_id != None:
            Students.objects.get(student_enrollment_id=id).delete()
            return redirect('AdminApp:students')
    except KeyError:
        return redirect('loginpage')
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def subjects(Http_req):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            if Http_req.method=="POST":
                subject_name=Http_req.POST['subject_name']
                subject_class=Http_req.POST['subject_class']
                subject_book=Http_req.POST['subject_book']
                subject_techer=Http_req.POST['subject_techer']
                subject=Subjects(subject_name=subject_name,subject_class=subject_class,subject_book=subject_book,subject_techer=subject_techer)
                subject.save()
                return redirect('AdminApp:subjects')
            cl=classes.objects.all()
            sub=Subjects.objects.all()
            return render(Http_req,'subjects.html',{'user_id':user_id,'cl':cl,'sub':sub})
    except KeyError:
        return redirect('loginpage')
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def admin_logout(http_req):
    try:
       if http_req.session['user_id'] != None:
           del http_req.session['user_id']
           return redirect('loginpage')
    except KeyError:
        return redirect('loginpage')

''' deletion '''
def delete_enq(http_req,id):
    user_id=http_req.session['user_id']
    try:
        if user_id != None:
            Enquiry.objects.get(id=id).delete()
            return redirect('AdminApp:view_enq')
    except KeyError:
        return redirect('loginpage')

    
''' Edit Class View'''
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editclass(Http_req,id):
    user_id=Http_req.session['user_id']
   # classes.objects.filter(class_id=id).update(class_name=)
    try:
        if user_id != None:
            cls=classes.objects.get(class_id=id)
            if Http_req.method=='POST':
                class_name=Http_req.POST['class_name']
                class_seats=Http_req.POST['class_seats']
                class_location=Http_req.POST['class_location']
                class_subjects=Http_req.POST['class_subjects']
                class_teacher=Http_req.POST['class_teacher']
                classes.objects.filter(class_id=id).update(class_name=class_name,class_seats=class_seats,class_location=class_location,class_subjects=class_subjects,class_teacher=class_teacher)
                return redirect('AdminApp:viewclasses')
            return render(Http_req,'editclass.html',{'user_id':user_id,'cls':cls})
    except KeyError:
        return redirect('loginpage')    
def edit_subjects(Http_req,id):
        user_id=Http_req.session['user_id']
        try:
            if user_id != None:
                ks=Subjects.objects.get(subject_id=id)
                if Http_req.method=="POST":
                    subject_name=Http_req.POST['subject_name']
                    subject_class=Http_req.POST['subject_class']
                    subject_book=Http_req.POST['subject_book']
                    subject_techer=Http_req.POST['subject_techer']
                    Subjects.objects.filter(subject_id=id).update(subject_name=subject_name,subject_class=subject_class,subject_book=subject_book,subject_techer=subject_techer)
                    
                    return redirect('AdminApp:subjects')
                return render(Http_req,'edit_subjects.html',{'user_id':user_id,'ks':ks})
        except KeyError:
            return redirect('loginpage')
def edit_students(Http_req,id):
    user_id=Http_req.session['user_id']
    try:
        if user_id != None:
            sts=Students.objects.get(student_enrollment_id=id)
            if Http_req.method=="POST":
            
            
                student_adhar=Http_req.POST['student_adhar']
                student_name=Http_req.POST['student_name']
                student_father_name=Http_req.POST['student_father_name']
                student_mother_name=Http_req.POST['student_mother_name']
                student_gender=Http_req.POST['student_gender']
                student_dob=Http_req.POST['student_dob']
                student_phone=Http_req.POST['student_phone']
                student_parents_phone=Http_req.POST['student_parents_phone']
                student_email=Http_req.POST['student_email']
                student_class=Http_req.POST['student_class']
                student_address=Http_req.POST['student_address']
                student_fee=Http_req.POST['student_fee']
                student_subjects=Http_req.POST['student_subjects']
                
                Students.objects.filter(student_enrollment_id=id).update(
                        student_adhar=student_adhar,
                        student_name=student_name,
                        student_father_name=student_father_name,
                        student_mother_name=student_mother_name,
                        student_gender=student_gender,
                        student_dob=student_dob,
                        student_phone=student_phone,
                        student_parents_phone=student_parents_phone,
                        student_email=student_email,
                        student_class=student_class,
                        student_address=student_address,
                        student_fee=student_fee,
                        student_subjects=student_subjects,
                        )
                
                return redirect('AdminApp:students')
            cls=classes.objects.all()
            return render(Http_req,'edit_students.html',{'user_id':user_id,'cls':cls,'sts':sts})
    except KeyError:
         return redirect('loginpage')
def delete_class(http_req,id):
    user_id=http_req.session['user_id']
    try:
        if user_id != None:
            classes.objects.get(class_id=id).delete()
            return redirect('AdminApp:viewclasses')
    except KeyError:
        return redirect('loginpage')
def delete_subject(http_req,id):
    user_id=http_req.session['user_id']
    try:
        if user_id != None:
            Subjects.objects.get(subject_id=id).delete()
            return redirect('AdminApp:subjects')
    except KeyError:
        return redirect('loginpage')

