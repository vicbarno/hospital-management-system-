from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Hospital System Backend!")
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hospital System API</h1><p>The backend is active.</p>")
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
from django.contrib import admin
from django.urls import path, include # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # This routes the homepage to your core app
]
