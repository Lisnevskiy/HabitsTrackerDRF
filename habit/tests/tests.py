from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from habit.models import Habit


class HabitAPITestCase(APITestCase):
    def setUp(self):
        # Создайте тестового пользователя (или используйте fixture)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_habit(self):
        # Отправляем POST-запрос для создания привычки
        data = {
            'user': self.user.id,
            'place': 'Home',
            'time': '10:00:00',
            'action': 'Exercise',
            'is_nice': True,
            'periodicity_days': 7,
            'execution_times': 60,
            'is_public': True
        }
        response = self.client.post('/api/v1/habit/', data, format='json')

        # Проверяем, что запрос вернул HTTP-код 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем, что запись была создана в базе данных
        self.assertEqual(Habit.objects.count(), 1)