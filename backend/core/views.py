from django.shortcuts import render
from django.http import JsonResponse
from patients.models import Patient


def dashboard_view(request):
    total_patients = Patient.objects.count()
    return render(request, 'dashboard.html', {
        'total_patients': total_patients,
    })


def home_view(request):
    return JsonResponse({'message': 'Welcome to Hospital Management System API'})
