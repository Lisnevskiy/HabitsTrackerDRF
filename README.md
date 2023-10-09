# Трекер полезных привычек

API SPA трекера полезных привычек. Сервис поддерживает работу с периодическими задачами(Celery Beat)
для напоминания о том, в какое время какие привычки необходимо выполнять.
Для рассылки уведомлений реализована интеграция с мессенджером Telegram.

## Используемые технологии
- Django Rest Framework (DRF)
- PostgreSQL
- Swagger
- CORS
- JSON Web Token Authentication
- telebot.TeleBot
- APITestCase
- Redis
- Celery Beat

## Установка и запуск

- Клонируйте репозиторий на вашем компьютере:
`git clone https://github.com/Lisnevskiy/HabitsTrackerDRF.git`
- Установите зависимости:
`pip install -r requirements.txt`
- Необходимые примеры переменных окружения указаны в файле [.env.sample](.env.sample)
- Выполните миграции базы данных:
`python manage.py migrate`
- Создайте суперпользователя `python manage.py create_sup_us`
- Запустите сервер:
`python manage.py runserver`
- Запустите Телеграм бот:
`python manage.py run_tg_bot`
- Запустите Celery и Celery Beat:
`celery -A config worker --loglevel=info`
`celery -A config beat --loglevel=info`

## Документация:
*/api/v1/swagger/*

*/api/v1/redoc/*
