from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def add_patient(request):
    if request.method == 'POST':
        Patient.objects.create(
            first_name=request.POST.get('first_name', '').strip(),
            last_name=request.POST.get('last_name', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            age=request.POST.get('age') or 0,
            gender='Unknown',
        )
        return redirect('patient_list')

    return render(request, 'add_patient.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {
        'patients': patients,
    })
