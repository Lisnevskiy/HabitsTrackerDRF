from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from habit.models import Habit
from users.models import User


class BaseSetup(APITestCase):
    """
    Базовый класс для настройки среды тестирования API.
    """
    def setUp(self):
        """
        Метод настройки тестовой среды.
        Инициализирует пользователя и создает привычку для использования в тестах API.
        """
        self.user = User.objects.create_user(username='user', password='password')
        access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        self.habit = Habit.objects.create(
            user=self.user,
            place="At home",
            time="13:00:00",
            action='cleaning',
            is_nice=False,
            periodicity_days=1,
            reward=None,
            execution_times=120,
            is_public=True
        )
