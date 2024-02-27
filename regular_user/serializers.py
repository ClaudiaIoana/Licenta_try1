from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from regular_user.models import RegularUser


class RegularUserSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        fields = ['id', 'username', 'email', 'password', 'profile_picture']


class AuthentificationSerializer(LoginSerializer, serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = RegularUser
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = self._validate_username(username, password)
        if user is None:
            msg = 'Unable to log in with provided credentials.'
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs


class RegularUserSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save()
