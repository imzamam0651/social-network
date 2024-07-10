from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from social.serializers import LoginSerializer

USER_MODEL = get_user_model()


class LoginAPIView(APIView):

    permission_classes = []

    def post(self, request):
        serializer_data = LoginSerializer(data=request.POST)
        if serializer_data.is_valid():
            data = serializer_data.validated_data
            user = User.objects.get(email=data["email"])
            if user:
                if user.check_password(data["password"]):
                    login(request, user)
                    user.save()
                    return Response(serializer_data.data, status=status.HTTP_200_OK)
                return Response({"message": "You are successfully loged in !!!"})
            return Response({"detail": "user does not exists"})
        return Response(
            {"errors": serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST
        )
