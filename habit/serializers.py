from rest_framework import serializers

from habit.models import Habit
from habit.validators import RelatedHabitAndRewardValidator, ExecutionTimeValidator, RelatedHabitValidator, \
    NiceHabitValidator, PeriodicityDaysValidator


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = ('pk', 'user', 'related_habit', 'place', 'time', 'action', 'is_nice',
                  'periodicity_days', 'reward', 'execution_times', 'is_public')

        validators = [
            RelatedHabitAndRewardValidator(),
            ExecutionTimeValidator(),
            RelatedHabitValidator(),
            NiceHabitValidator(),
            PeriodicityDaysValidator()
        ]
