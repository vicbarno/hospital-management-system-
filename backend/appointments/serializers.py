from rest_framework import serializers

from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.__str__', read_only=True)
    doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'date', 'time', 'status']
