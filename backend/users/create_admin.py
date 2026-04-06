import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'kiptoobarno@gmail.com'
ADMIN_PASSWORD = 'admin123'

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD,
    )
    print("✅ Admin user created")
else:
    print("⚠️ Admin already exists")