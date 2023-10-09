from rest_framework import status

from habit.tests.base_setup import BaseSetup


class ValidatorAPITestCase(BaseSetup):

    def test_related_habit_and_reward_validator(self):
        data = {
            "user": self.user.id,
            "related_habit": self.habit.pk,
            "place": "Квартира",
            "time": "14:00:00",
            "action": "Уборка",
            "is_nice": False,
            "periodicity_days": 1,
            "reward": "Some reward",
            "execution_times": 120,
            "is_public": True
        }

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'Нельзя одновременно выбрать связанную привычку и указать вознаграждение!',
            response.data.get('non_field_errors')
        )

    def test_execution_time_validator(self):
        data = {
            "user": self.user.id,
            "related_habit": None,
            "place": "Квартира",
            "time": "14:00:00",
            "action": "Уборка",
            "is_nice": False,
            "periodicity_days": 1,
            "reward": "",
            'execution_times': 150,
            "is_public": True
        }

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'Время выполнения привычки не может превышать 120 секунд!',
            response.data.get('non_field_errors')
        )

    def test_related_habit_validator(self):
        data = {
            "user": self.user.pk,
            "related_habit": self.habit.pk,
            "place": "Квартира",
            "time": "14:00:00",
            "action": "Уборка",
            "is_nice": False,
            "periodicity_days": 1,
            "reward": "",
            "execution_times": 120,
            "is_public": True
        }

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'Связанная привычка должна иметь признак приятной привычки!',
            response.data.get('non_field_errors')
        )

    def test_nice_habit_validator(self):
        data = {
            "user": self.user.id,
            "related_habit": None,
            "place": "Квартира",
            "time": "14:00:00",
            "action": "Уборка",
            "is_nice": True,
            "periodicity_days": 1,
            "reward": "Some reward",
            "execution_times": 120,
            "is_public": True
        }

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'У приятной привычки не может быть вознаграждения или связанной привычки!',
            response.data.get('non_field_errors')
        )

    def test_periodicity_days_validator(self):
        data = {
            "user": self.user.id,
            "related_habit": None,
            "place": "Квартира",
            "time": "14:00:00",
            "action": "Уборка",
            "is_nice": False,
            "periodicity_days": 8,
            "reward": "",
            "execution_times": 120,
            "is_public": True
        }

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'Периодичность не должна превышать 7 дней!',
            response.data.get('non_field_errors')
        )

        data["periodicity_days"] = 0

        response = self.client.post('/api/v1/habit/', data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'Периодичность не может быть меньше или равна нулю!',
            response.data.get('non_field_errors')
        )
