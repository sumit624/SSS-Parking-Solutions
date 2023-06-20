from contextlib import nullcontext
from django.db import models

# Create your models here.
class savedata(models.Model):
    name=models.CharField(max_length=30)
    vehicle_no=models.IntegerField()
    license_no=models.IntegerField()
    aadhar_no=models.IntegerField()
    model=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=15, null=True)