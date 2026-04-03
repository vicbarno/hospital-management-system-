from django.shortcuts import render
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({'message': 'Welcome to Hospital Management System API'})
