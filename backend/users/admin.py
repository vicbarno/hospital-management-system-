from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.site_header = "Mvita Comprehensive Health Centre"
admin.site.site_title = "Mvita Admin Portal"
admin.site.index_title = "Welcome to Mvita HMS"

admin.site.register(User)
