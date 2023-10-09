from django.urls import path
from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitViewSet, HabitPublicListView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [
    path('habit/public/', HabitPublicListView.as_view(), name='habit_public')
] + router.urls
