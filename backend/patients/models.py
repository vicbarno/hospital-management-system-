from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):

    # Patient Identification
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    patient_id = models.CharField(max_length=50, unique=True)
    visit_datetime = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)

    # Chief Complaint
    chief_complaint = models.TextField(blank=True)
    complaint_duration = models.CharField(max_length=50, blank=True)

    # History of Presenting Illness (HPI)
    hpi_onset = models.DateTimeField(null=True, blank=True)
    hpi_description = models.TextField(blank=True)
    pain_scale = models.IntegerField(null=True, blank=True)
    associated_symptoms = models.TextField(blank=True)

    # Past Medical History (PMH)
    chronic_conditions = models.CharField(max_length=255, blank=True)  # comma-separated
    previous_admissions = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)

    # Past Surgical History (PSH)
    surgery_name = models.CharField(max_length=255, blank=True)
    surgery_date = models.DateField(null=True, blank=True)
    surgery_notes = models.TextField(blank=True)

    # Family History
    family_history = models.CharField(max_length=255, blank=True)  # comma-separated

    # Social History
    smoker = models.BooleanField(default=False)
    alcohol_use = models.CharField(max_length=100, blank=True)
    drug_use = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    living_situation = models.CharField(max_length=255, blank=True)

    # Economic History
    employment_status = models.CharField(max_length=100, blank=True)
    insurance_type = models.CharField(max_length=100, blank=True)
    financial_constraints = models.BooleanField(default=False)
    economic_notes = models.TextField(blank=True)

    # Review of Systems (ROS)
    ros_general = models.CharField(max_length=255, blank=True)
    ros_respiratory = models.CharField(max_length=255, blank=True)
    ros_cardiovascular = models.CharField(max_length=255, blank=True)
    ros_gi = models.CharField(max_length=255, blank=True)
    ros_neurological = models.CharField(max_length=255, blank=True)

    medical_history = models.TextField(blank=True)  # keep for legacy

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    