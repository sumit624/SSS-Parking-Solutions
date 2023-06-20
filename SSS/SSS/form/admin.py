from django.contrib import admin

# Register your models here.

from django.contrib.admin.sites import site
from form.models import savedata

class savedataadmin(admin.ModelAdmin):
    list_display=('name','vehicle_no','license_no','aadhar_no','model','email','password')

admin.site.register(savedata,savedataadmin)