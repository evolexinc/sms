from django.shortcuts import render, redirect
from .models import Enquiry, admin_data
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from AdminApp.models import *


# Create your views here.
def home(http_req):
    nf=Notifications.objects.all()
    return render(http_req, "home.html",{ 'nf':nf})


def about(http_req):
    return render(http_req, "about.html")


def contact(http_req):
    return render(http_req, "contact.html")


def layout(http_req):
    return render(http_req, "layout.html")


""" POST DATA"""


def save(req):
    name = req.POST["name"]
    gender = req.POST["gender"]
    address = req.POST["address"]
    contact_number = req.POST["contact_number"]
    email = req.POST["email"]
    enquiry_text = req.POST["enquiry_text"]
    timeDATA = timezone.now()
    ds = Enquiry(
        name=name,
        gender=gender,
        address=address,
        contact_number=contact_number,
        email=email,
        enquiry_text=enquiry_text,
        enquiry_date=timeDATA,
    )
    ds.save()
    return redirect("Contactus")


def login(req):
    return render(req, "login.html")


def admin_login(reqs):
    if reqs.method == "POST":
        user_type = reqs.POST["user_type"]
        user_id = reqs.POST["user_id"]
        passkey = reqs.POST["passkey"]
        if user_type == "admin":
            try:
                user = admin_data.objects.get(user_id=user_id, passkey=passkey)
                if user is not None:
                    reqs.session["user_id"] = user_id
                    return redirect("AdminApp:Dashboard")
            except ObjectDoesNotExist:
                return render(reqs, "login.html", {"msg": "INValid User"})
        elif user_type == "teacher":
            try:
                teacher = Teachers.objects.get(
                    teacher_id=user_id, teacher_password=passkey
                )
                if teacher != None:
                    reqs.session["user_id"] = user_id
                    return redirect("TeacherApp:Teacher_Dashboard")
            except ObjectDoesNotExist:
                return render(reqs, "login.html", {"msg": "Invalid user"})
        elif user_type == "student":
            try:
                student = Students.objects.get(
                    student_email=user_id, student_password=passkey
                )
                if student != None:
                    reqs.session["user_id"] = user_id
                    return redirect("StudentApp:Student_Dashboard")
            except ObjectDoesNotExist:
                return render(reqs, "login.html", {"msg": " Invalid user"})
        else:
            return render(reqs, "login.html", {"msg": " !Login type dose not exist"})


def about_jaipuria(http_req):
    return render(http_req, "about_jaipuria.html")


def acadmics(http_req):
    return render(http_req, "acadmics.html")


def chairman(http_req):
    return render(http_req, "chairman.html")


def Circular(http_req):
    return render(http_req, "Circular.html")


def Contactus(http_req):
    return render(http_req, "Contact-us.html")


def medicalroom(http_req):
    return render(http_req, "f_medicalroom.html")


def f_transport(http_req):
    return render(http_req, "f_transport.html")


def facilities(http_req):
    return render(http_req, "facilities.html")


def about_founder(http_req):
    return render(http_req, "about_founder.html")

def about_principal(http_req):
    return render(http_req, "about_principal.html")

def about_management(http_req):
    return render(http_req, "about_management.html")

def news_events(http_req):
    return render(http_req, "news_events.html")
