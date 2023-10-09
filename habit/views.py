from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitSetPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления привычками пользователя.
    Позволяет создавать, читать, обновлять и удалять привычки.
    Привязан к конкретному пользователю (только его привычки).
    """
    serializer_class = HabitSerializer
    pagination_class = HabitSetPagination
    permission_classes = (IsOwner, IsAuthenticated)

    def get_queryset(self):
        """
        Получить набор привычек конкретного пользователя.
        """
        return Habit.objects.filter(user=self.request.user.pk)


class HabitPublicListView(generics.ListAPIView):
    """
    Публичный список привычек.
    Отображает список публичных привычек для всех пользователей.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitSetPagination

    def get_queryset(self):
        """
        Получить набор публичных привычек.
        """
        return Habit.objects.filter(is_public=True)
