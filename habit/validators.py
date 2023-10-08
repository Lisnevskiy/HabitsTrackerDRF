from rest_framework.serializers import ValidationError
from habit.models import Habit


class RelatedHabitAndRewardValidator:
    """
    Валидатор, проверяющий, что не указаны одновременно связанная привычка и вознаграждение.
    Raises:
        ValidationError: Если связанная привычка и вознаграждение указаны вместе.
    """
    def __call__(self, data):
        related_habit = data.get('related_habit')
        reward = data.get('reward')

        if related_habit and reward:
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и указать вознаграждение!')


class ExecutionTimeValidator:
    """
    Валидатор, проверяющий, что время выполнения привычки не превышает 120 секунд.
    Raises:
        ValidationError: Если время выполнения привычки превышает 120 секунд.
    """
    def __call__(self, data):
        execution_time = data.get('execution_times')

        if not execution_time:
            raise ValidationError('Время выполнения должно быть указано!')

        if execution_time > 120:
            raise ValidationError('Время выполнения привычки не может превышать 120 секунд!')


class RelatedHabitValidator:
    """
    Валидатор, проверяющий, что связанная привычка имеет признак приятной привычки.
    Raises:
        ValidationError: Если связанная привычка не имеет признак приятной привычки.
    """
    def __call__(self, data):
        related_habit = data.get('related_habit')

        if related_habit:
            related_habit = Habit.objects.get(pk=related_habit.pk)

            if related_habit.is_nice is False:
                raise ValidationError('Связанная привычка должна иметь признак приятной привычки!')


class NiceHabitValidator:
    """
    Валидатор, проверяющий, что у приятной привычки нет связанной привычки или вознаграждения.
    Raises:
        ValidationError: Если у приятной привычки есть связанная привычка или вознаграждение.
    """
    def __call__(self, data):
        nice_habit = data.get('is_nice')

        if nice_habit:
            related_habit = data.get('related_habit')
            reward = data.get('reward')

            if related_habit or reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки!')


class PeriodicityDaysValidator:
    """
    Валидатор, проверяющий, что периодичность не превышает 7 дней и не меньше или равна нулю.
    Raises:
        ValidationError: Если периодичность превышает 7 дней или меньше или равна нулю.
    """
    def __call__(self, data):
        periodicity_days = data.get('periodicity_days')

        if periodicity_days > 7:
            raise ValidationError('Периодичность не должна превышать 7 дней!')

        if periodicity_days <= 0:
            raise ValidationError('Периодичность не может быть меньше или равна нулю!')
