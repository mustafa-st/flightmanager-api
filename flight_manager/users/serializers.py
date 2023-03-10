import phonenumbers
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from flight_manager.users.models import User


class UserRegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(allow_blank=True, max_length=150)
    last_name = serializers.CharField(allow_blank=True, max_length=150)
    username = serializers.CharField()
    mobile_number = serializers.CharField()
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=128, min_length=8)

    def validate_mobile_number(self, value):
        phone_number = phonenumbers.parse(str(value))
        if not phonenumbers.is_possible_number(phone_number):
            raise Exception
        return phone_number

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            mobile_number=validated_data["mobile_number"],
        )
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=128)


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
