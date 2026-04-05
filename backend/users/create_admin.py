import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='kiptoobarno@gmail.com',
        password='Admin123!'
    )
    print("✅ Admin user created")
else:
    print("⚠️ Admin already exists")