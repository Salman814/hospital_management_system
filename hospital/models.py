from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    doctor_id = models.IntegerField()
    speciality = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return self.first_name