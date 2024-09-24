from django.db import models
from AdminApp.models import Teachers


# Create your models here.
class Enquiry(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=225)  # 225 is a default value
    gender = models.CharField(max_length=10)  # 10 used for fixed size
    address = models.CharField(max_length=500)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    enquiry_text = models.CharField(max_length=1000)

    enquiry_date = models.DateTimeField(auto_created=True)


""" Model for Admin"""


class admin_data(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)
    passkey = models.CharField(max_length=30)


""" for Techer Login """
