from rest_framework.routers import DefaultRouter

from habit.views import HabitViewSet

router = DefaultRouter()
router.register(r'habit', HabitViewSet)

urlpatterns = router.urls
