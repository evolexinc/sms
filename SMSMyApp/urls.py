from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("layout", layout, name="layout"),
    path("", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("enqsave", save, name="enqsave"),
    path("login", login, name="loginpage"),
    path("adminlogin", admin_login, name="adminlogin"),
    path("about_jaipuria", about_jaipuria, name="about_jaipuria"),
    path("acadmics", acadmics, name="acadmics"),
    path("chairman", chairman, name="chairman"),
    path("Circular", Circular, name="Circular"),
    path("Contactus", Contactus, name="Contactus"),
    path("medicalroom", medicalroom, name="medicalroom"),
    path("f_transport", f_transport, name="f_transport"),
    path("facilities", facilities, name="facilities"),
    path("news_events", news_events, name="news_events"),
]
