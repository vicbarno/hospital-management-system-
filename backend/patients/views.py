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
            age=request.POST.get('age') or 0,
            dob=request.POST.get('dob') or None,
            gender=request.POST.get('gender', '').strip(),
            patient_id=request.POST.get('patient_id', '').strip(),
            visit_datetime=request.POST.get('visit_datetime') or None,
            phone=request.POST.get('phone', '').strip(),
            chief_complaint=request.POST.get('chief_complaint', '').strip(),
            complaint_duration=request.POST.get('complaint_duration', '').strip(),
            hpi_onset=request.POST.get('hpi_onset') or None,
            hpi_description=request.POST.get('hpi_description', '').strip(),
            pain_scale=request.POST.get('pain_scale') or None,
            associated_symptoms=request.POST.get('associated_symptoms', '').strip(),
            chronic_conditions=request.POST.get('chronic_conditions', '').strip(),
            previous_admissions=request.POST.get('previous_admissions', '').strip(),
            current_medications=request.POST.get('current_medications', '').strip(),
            allergies=request.POST.get('allergies', '').strip(),
            surgery_name=request.POST.get('surgery_name', '').strip(),
            surgery_date=request.POST.get('surgery_date') or None,
            surgery_notes=request.POST.get('surgery_notes', '').strip(),
            family_history=request.POST.get('family_history', '').strip(),
            smoker=True if request.POST.get('smoker') == 'on' else False,
            alcohol_use=request.POST.get('alcohol_use', '').strip(),
            drug_use=request.POST.get('drug_use', '').strip(),
            marital_status=request.POST.get('marital_status', '').strip(),
            occupation=request.POST.get('occupation', '').strip(),
            living_situation=request.POST.get('living_situation', '').strip(),
            employment_status=request.POST.get('employment_status', '').strip(),
            insurance_type=request.POST.get('insurance_type', '').strip(),
            financial_constraints=True if request.POST.get('financial_constraints') == 'on' else False,
            economic_notes=request.POST.get('economic_notes', '').strip(),
            ros_general=request.POST.get('ros_general', '').strip(),
            ros_respiratory=request.POST.get('ros_respiratory', '').strip(),
            ros_cardiovascular=request.POST.get('ros_cardiovascular', '').strip(),
            ros_gi=request.POST.get('ros_gi', '').strip(),
            ros_neurological=request.POST.get('ros_neurological', '').strip(),
        )
        return redirect('patient_list')

    return render(request, 'add_patient.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {
        'patients': patients,
    })
