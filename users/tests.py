from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.models import User


class UserRegisterAPITestCase(APITestCase):
    def test_register_user(self):
        """
        Тест регистрации нового пользователя через API.
        Создает пользователя через API и проверяет, что:
        1. HTTP-код ответа равен 201 (Created).
        2. Количество объектов User в базе данных увеличивается на 1.
        3. Данные пользователя соответствуют ожидаемым значениям.
        """
        data = {
            'username': 'new_user',
            'password': 'new_password',
        }
        response = self.client.post(reverse('users:users_register'), data, format='json')

        # Проверка HTTP-кода ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка увеличения количества объектов User в базе данных
        self.assertEqual(User.objects.count(), 1)

        # Получение созданного пользователя из базы данных
        new_user = User.objects.get(username='new_user')

        # Проверка данных пользователя
        self.assertEqual(new_user.username, 'new_user')
        self.assertTrue(new_user.check_password('new_password'))
        # (Дополнительные проверки по данным пользователя могут быть добавлены согласно вашим требованиям)
