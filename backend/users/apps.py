from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model

ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'kiptoobarno@gmail.com'
ADMIN_PASSWORD = 'admin123'


def create_default_admin(sender, **kwargs):
    User = get_user_model()
    if not User.objects.filter(username=ADMIN_USERNAME).exists():
        User.objects.create_superuser(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            password=ADMIN_PASSWORD,
        )
        print("✅ Admin user created")
    else:
        print("⚠️ Admin already exists")


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        post_migrate.connect(create_default_admin, sender='users')

