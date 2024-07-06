from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=21, required=True)
    password = serializers.CharField(
        required=False, allow_null=True, write_only=True
    )  # noka: E501;

    def validate(self, attrs):
        email = attrs.get("email")
        user = User.objects.filter(email=email).exists()
        if user:
            return attrs
        else:
            msg = {"detail": "User does not exists.", "register": True}
            raise serializers.ValidationError(msg, code="authorization")
