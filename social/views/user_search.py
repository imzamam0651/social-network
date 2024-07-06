from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from social.serializers import UserSerializer

USER_MODEL = get_user_model()


class UserSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keyword = request.query_params.get("keyword")
        queryset = USER_MODEL.objects.filter(username__icontains=keyword)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
