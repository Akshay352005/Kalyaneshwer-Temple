import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

email = 'akshayvhegde05@gmail.com'
password = 'Akshay@1234'
username = email.split('@')[0]

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully.")
else:
    u = User.objects.get(username=username)
    u.email = email
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print(f"Superuser '{username}' updated successfully.")
