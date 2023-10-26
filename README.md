# Трекер полезных привычек

API SPA трекера полезных привычек. Сервис поддерживает работу с периодическими задачами(Celery Beat)
для напоминания о том, в какое время какие привычки необходимо выполнять.
Для рассылки уведомлений реализована интеграция с мессенджером Telegram.
Есть возможность запуска с помощью Docker.
Имеется инструкция по запуску приложения на удаленном сервере.

## Используемые технологии
- Django Rest Framework (DRF)
- Docker
- Docker Compose
- PostgreSQL
- Swagger
- CORS
- JSON Web Token Authentication
- telebot.TeleBot
- APITestCase
- Redis
- Celery Beat

## Установка и запуск локально

- Клонируйте репозиторий на вашем компьютере:
```bash
- git clone https://github.com/Lisnevskiy/HabitsTrackerDRF.git`
```
- Установите зависимости:
`pip install -r requirements.txt`
- Необходимые примеры переменных окружения указаны в файле [.env.sample](.env.sample)
- В настройках приложения [config/settings.py](config/settings.py) в разделе DATABASES удалите строку "HOST": "db"
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

## Установка и запуск локально с помощью Docker
Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- Docker
- Docker Compose

1. Клонируйте репозиторий на вашем компьютере:
```bash 
git clone https://github.com/Lisnevskiy/HabitsTrackerDRF.git`
```
2. Создайте файл .env в корневой директории проекта и укажите в нем необходимые переменные окружения, пример которых указан в файле [.env.sample](.env.sample). 
Убедитесь, что значения переменных окружения соответствуют вашей конфигурации.

3. Запустите проект, используя Docker Compose:

```bash
docker-compose up --build
```

# Руководство по развертыванию проекта на удаленном сервере

Это руководство предоставляет инструкции для развертывания проекта HabitsTrackerDRF на удаленном сервере. Проект использует Docker и Docker Compose для удобного управления контейнерами.

## Требования

Перед тем как начать, убедитесь, что на вашем удаленном сервере установлены следующие компоненты:

- Docker
- Docker Compose

## Шаг 1: Клонирование репозитория

Сначала клонируйте репозиторий проекта на ваш удаленный сервер:

```bash
git clone https://github.com/Lisnevskiy/HabitsTrackerDRF.git
cd HabitsTrackerDRF
```

## Шаг 2: Создание файла конфигурации
Создайте файл .env в корневой директории проекта и укажите в нем необходимые переменные окружения, пример которых указан в файле [.env.sample](.env.sample)

Убедитесь, что значения переменных окружения соответствуют вашей конфигурации.

## Шаг 3: Запуск проекта
Теперь можно запустить проект, используя Docker Compose:

```bash
docker-compose up -d --build
```
Проект будет развернут, и вы сможете получить доступ к нему по IP-адресу вашего удаленного сервера и порту, указанному в Docker Compose файле.

## Завершение работы
Для завершения работы проекта и выключения контейнеров, выполните следующую команду:
```bash
docker-compose down
```

## Документация:
*/api/v1/swagger/*

*/api/v1/redoc/*
