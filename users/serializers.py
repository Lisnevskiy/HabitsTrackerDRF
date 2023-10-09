from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data['password']

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User

        fields = ('username', 'password', 'tg_chat_id')
