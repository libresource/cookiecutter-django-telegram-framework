from django.contrib.auth import get_user_model

User = get_user_model()


def create_admin(username, password, email):
    if User.objects.filter(username=username).exists():
        return User.objects.get(username=username), False
    return User.objects.create_superuser(username=username, password=password, email=email), True
