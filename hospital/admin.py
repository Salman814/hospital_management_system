from django.contrib import admin
from  .models import Doctor, Patients

# Register your models here.
admin.site.register(Doctor)

admin.site.register(Patients)