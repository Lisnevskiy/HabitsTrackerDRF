from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('pk', 'user', 'related_habit', 'place', 'time', 'action', 'is_nice',
                  'periodicity_days', 'reward', 'execution_times', 'is_public')
