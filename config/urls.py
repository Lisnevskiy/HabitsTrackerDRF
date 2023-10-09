from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Определение параметров для Swagger и ReDoc документации
schema_view = get_schema_view(
   openapi.Info(
      title="Habits Tracker API",
      default_version='v1',
      description="API для отслеживания привычек",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Панель администратора Django
    path("admin/", admin.site.urls),
    # Подключение URL-маршрутов приложения Habit
    path('api/v1/', include('habit.urls', namespace='habit')),
    # Подключение URL-маршрутов приложения Users
    path('api/v1/users/', include('users.urls', namespace='users')),
    # URL для доступа к Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # URL для доступа к ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
