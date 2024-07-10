from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_json_api import serializers
from rest_framework_json_api.views import viewsets

from social.models import FriendRequest
from social.serializers import FriendRequestSerializer


class FriendRequestViewset(viewsets.ModelViewSet):

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def initial(self, request, *args, **kwargs):
        # Add throttling if the request is a POST request
        # So that user cannot create more than 3 request in a minute
        if request.method == "POST":
            self.throttle_scope = "friend_requests"
        return super().initial(request, *args, **kwargs)

    def perform_create(self, serializer):
        data = serializer.validated_data

        if self.request.user != data.get("sender"):
            data["sender"] = self.request.user

        if data.get("sender") == data.get("receiver"):
            raise serializers.ValidationError(
                "you can't send friend request to yourself. Try different user."
            )

        queryset = self.queryset.filter(
            Q(sender=self.request.user, receiver=data.get("receiver"))
            | Q(sender=data.get("receiver"), receiver=self.request.user)
        )
        if queryset.exists():
            raise serializers.ValidationError(
                "you have already sent the friend request to this user. Try different user."
            )

        serializer.save()

    @action(detail=False, methods=["get"], url_path="friends")
    def accepted_friends_list(self, request):
        queryset = self.queryset.filter(
            Q(sender=request.user) | Q(receiver=request.user),
            status=FriendRequest.REQUEST_CHOICES.Accepted,
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="pending")
    def pending_friends_list(self, request):
        queryset = self.queryset.filter(
            Q(sender=request.user) | Q(receiver=request.user),
            status=FriendRequest.REQUEST_CHOICES.Pending,
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"], url_path="accept")
    def accept_friends_request(self, request, pk=None):
        instance = self.get_object()

        if request.user != instance.receiver:
            return Response(
                "You are not permitted to accept this friend request!",
                status=status.HTTP_403_FORBIDDEN,
            )

        if (
            instance.status == FriendRequest.REQUEST_CHOICES.Accepted
            or instance.status == FriendRequest.REQUEST_CHOICES.Rejected
        ):
            return Response(
                "You have already accepted / rejected this friend request!",
                status=status.HTTP_200_OK,
            )

        instance.status = FriendRequest.REQUEST_CHOICES.Accepted
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["put"], url_path="reject")
    def reject_friends_request(self, request, pk=None):
        instance = self.get_object()

        if request.user != instance.receiver:
            return Response(
                "You are not permitted to reject this friend request!",
                status=status.HTTP_403_FORBIDDEN,
            )

        if (
            instance.status == FriendRequest.REQUEST_CHOICES.Accepted
            or instance.status == FriendRequest.REQUEST_CHOICES.Rejected
        ):
            return Response(
                "You have already accepted / rejected this friend request!",
                status=status.HTTP_200_OK,
            )

        instance.status = FriendRequest.REQUEST_CHOICES.Rejected
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
