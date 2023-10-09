import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя (админа).
    Создает суперпользователя с заданными параметрами, такими как имя пользователя и пароль.
    """
    help = 'Create a superuser (admin) with specified username and password.'

    def handle(self, *args, **options):
        # Создание суперпользователя
        user = User.objects.create(
            username=os.getenv("ADMIN_NAME"),
            is_staff=True,
            is_superuser=True,
        )
        # Установка пароля для суперпользователя
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.save()
