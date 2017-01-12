from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_id = models.IntegerField()
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    avg_waiting_time = models.DurationField(null = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Appointment(models.Model):
    app_id = models.IntegerField()
    time_of_arrival = models.TimeField()
    start_time = models.TimeField()
    wait_time = models.DurationField()
