from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from patients.models import Patient
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary_view(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    status_counts = Appointment.objects.values('status').annotate(count=Count('id'))
    by_doctor = Appointment.objects.values('doctor__username').annotate(count=Count('id'))

    return Response({
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'appointments_by_status': {item['status']: item['count'] for item in status_counts},
        'appointments_by_doctor': {item['doctor__username']: item['count'] for item in by_doctor},
    })
