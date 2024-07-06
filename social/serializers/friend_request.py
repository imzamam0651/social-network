from rest_framework_json_api import serializers

from social.models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = "__all__"
        read_only_fields = ("sender",)
