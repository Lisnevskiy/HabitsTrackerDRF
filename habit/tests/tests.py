from rest_framework import status
from rest_framework.reverse import reverse

from habit.models import Habit
from habit.tests.base_setup import BaseSetup


class HabitAPITestCase(BaseSetup):
    def test_create_habit(self):
        """
        Тест создания новой привычки через API.
        Создает привычку через API и проверяет, что:
        1. HTTP-код ответа равен 201 (Created).
        2. Количество объектов Habit в базе данных увеличивается на 1.
        3. Строковое представление созданной привычки соответствует ожидаемому значению.
        4. Проверяет, что после создания привычки количество привычек в списке увеличивается на 1.
        """
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

        # Проверка HTTP-кода ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка увеличения количества объектов Habit в базе данных
        self.assertEqual(Habit.objects.count(), 2)

        # Тест GET запроса для получения списка привычек
        response = self.client.get('/api/v1/habit/')

        self.assertEqual(response.json()['count'], 2)

        # Создание привычки с теми же данными и проверка строки __str__
        data['user'] = self.user
        habit = Habit(**data)
        habit.save()

        expected_str = 'Exercise 10:00:00 Home'
        # Сравнение строки __str__ с ожидаемым значением
        self.assertEqual(str(habit), expected_str)

    def test_list_public_habits(self):
        """
        Тест получения списка публичных привычек через API.
        Создает привычку и проверяет, что она не отображается в списке публичных привычек.
        """
        # Создание привычки, не являющейся публичной
        Habit.objects.create(
            user=self.user,
            place="home",
            time="13:00:00",
            action='test',
            is_nice=False,
            periodicity_days=1,
            reward=None,
            execution_times=120,
            is_public=False
        )

        # Получение списка публичных привычек через API
        response = self.client.get(reverse('habit:habit_public'))

        # Проверка HTTP-кода ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка количества привычек в списке
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(len(response.json()['results']), 1)
