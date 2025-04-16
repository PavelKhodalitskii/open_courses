from rest_framework import serializers

from .models import ExtendedUser


class ExtendedUserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'username']
        model = ExtendedUser