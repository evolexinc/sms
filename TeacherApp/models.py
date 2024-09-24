from django.db import models
import datetime

# Create your models here.
class Study_Material(models.Model):
    Document_title=models.CharField(max_length=10)
    Document_location=models.FileField(upload_to='')
    Document_for_class=models.CharField(max_length=30)
    Uploaded_date=models.DateField(default=datetime.date.today())