from django.contrib import admin

from .models.friend_request import FriendRequest


class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ["sender", "receiver"]
    list_display = [
        "sender",
        "receiver",
    ]
    search_fields = ["sender__email", "receiver__email"]

    class Meta:
        model = FriendRequest


admin.site.register(FriendRequest, FriendRequestAdmin)
