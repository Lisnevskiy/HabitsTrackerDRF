from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='связанная привычка',
        **NULLABLE
    )

    place = models.CharField(max_length=255, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.TextField(verbose_name='действие')
    is_nice = models.BooleanField(verbose_name='признак приятной привычки')
    periodicity_days = models.BigIntegerField(default=1, verbose_name='периодичность (дни)')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    execution_times = models.BigIntegerField(default=120, verbose_name='время на выполнение')  # Измеряется в секундах.
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.action} {self.time} {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
