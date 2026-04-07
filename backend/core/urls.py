from django.urls import path
from . import views
from patients.views import add_patient, patient_list

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('patients/add/', add_patient, name='add_patient'),
    path('patients/list/', patient_list, name='patient_list'),
]
