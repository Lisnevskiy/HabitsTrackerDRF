from datetime import datetime

import telebot
from celery import shared_task

from config import settings
from habit.models import Habit

from users.models import User

TELEGRAM_MESSAGE = """
Привет! Это напоминание о привычке:
Вам нужно выполнить {habit.action}.
Местоположение: {habit.place}
"""


@shared_task
def send_telegram_notification():
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

    current_time = datetime.now().time()

    users = User.objects.filter(telegram_chat_id__isnull=False)

    for user in users:
        habits = Habit.objects.filter(user=user)

        for habit in habits:
            if habit.time.hour == current_time.hour and habit.time.minute == current_time.minute:
                message = TELEGRAM_MESSAGE.format(habit.action, habit.place)

                bot.send_message(user.telegram_chat_id, message)
