from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import ExtendedUser


class ExtendedUserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'username']
        model = ExtendedUser

class EmailAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True)

    def validate(self, data):
        email = data['email']
        password = data['password']

        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            raise serializers.ValidationError('Не найдено пользователя с предоставленными данными')

        data['user'] = user
        return data