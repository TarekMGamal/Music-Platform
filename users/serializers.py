from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.core.validators import validate_email


class user_serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, label="Confirm password")

    def create(self, validated_data):
        custom_user_model = get_user_model()
        
        user = custom_user_model.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        
        password_validation.validate_password(data.get('password'), user=self.instance)
        validate_email(data.get('email'))
        
        return data

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "confirm_password")