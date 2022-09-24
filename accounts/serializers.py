# Serializers define the API representation.
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault, Serializer

from .models import User, UserAddress


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )


class AddressSerializer(ModelSerializer):
    user = HiddenField(
        default=CurrentUserDefault()
    )

    class Meta:
        model = UserAddress
        fields = [
            "user",
            "building",
            "street_1",
            "street_2",
        ]

