import telebot
from django.conf import settings
from django.core.management import BaseCommand


from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(
                message.chat.id,
                'Привет! Чтобы бот мог присылать уведомления о привычках напишите свое имя пользователя, '
                'которое вы указывали при регистрации.'
            )

        @bot.message_handler(func=lambda message: True)
        def handle_email_input(message):
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
