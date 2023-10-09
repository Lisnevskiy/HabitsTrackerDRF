from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class UserRegisterView(generics.CreateAPIView):
    """
    Представление для регистрации новых пользователей.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
