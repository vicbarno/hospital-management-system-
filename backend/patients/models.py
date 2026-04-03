from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
    