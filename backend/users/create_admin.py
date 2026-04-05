from django.contrib.auth import get_user_model

User = get_user_model()

username = "victor"
email = "kiptoobarno@gmail.com"
password = "Victor1234"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("✅ Superuser created successfully")
else:
    print("⚠️ Admin already exists")