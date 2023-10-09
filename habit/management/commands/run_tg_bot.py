import telebot
from django.conf import settings
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Django-команда управления для запуска Telegram-бота для уведомлений о привычках.
    """
    def handle(self, *args, **options):
        """
        Метод обработки для команды управления.
        Инициализирует и запускает Telegram-бота, позволяя пользователям связать свои имена пользователя для
        получения уведомлений о привычках.
        """
        bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            """
            Обрабатывает команду /start и отправляет приветственное сообщение.
            """
            bot.send_message(
                message.chat.id,
                'Привет! Чтобы бот мог присылать уведомления о привычках, напишите свое имя пользователя, '
                'которое вы указали при регистрации.'
            )

        @bot.message_handler(func=lambda message: True)
        def handle_username_input(message):
            """
            Обрабатывает входные данные пользователя и связывает их чат Telegram с их именем пользователя.
            """
            chat_id = message.chat.id
            username = message.text

            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                user.tg_chat_id = chat_id
                user.save()

                bot.send_message(chat_id,
                                 'Ваше имя пользователя подтверждено. Теперь бот будет присылать уведомления.'
                                 )
            else:
                bot.send_message(chat_id, text='Пользователя с таким именем не обнаружено!')

        bot.infinity_polling()
