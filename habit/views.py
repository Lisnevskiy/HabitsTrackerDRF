from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitSetPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitSetPagination
    permission_classes = (IsOwner, IsAuthenticated)

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user.pk)


class HabitPublicListView(generics.ListAPIView):
    queryset = queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitSetPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
    