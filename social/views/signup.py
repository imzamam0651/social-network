from django.contrib.auth import get_user_model, login
from rest_framework import status
from rest_framework.permissions import AllowAny  # noqa: F401;
from rest_framework.response import Response
from rest_framework.views import APIView

from social.serializers import UserSerializer

USER_MODEL = get_user_model()


class SignupAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        # import pdb; pdb.set_trace()

        email = request.POST.get("email")
        if USER_MODEL.objects.filter(email=email).exists():
            return Response(
                {"errors": f"This user ({email}) already exists !!!"},
                status=status.HTTP_400_BAD_REQUEST,
            )  # noqa: E501;

        request.data._mutable = True
        request.data["username"] = email
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(
                {"message": "You are successfully signed in !!!"},
                status=status.HTTP_200_OK,
            )  # noqa: E501;
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )  # noqa: E501;
