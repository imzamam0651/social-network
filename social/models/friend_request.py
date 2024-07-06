from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices

USER_MODEL = get_user_model()


class FriendRequest(models.Model):
    """FriendRequest Model"""

    DEFAULT_REQUEST = "Pending"
    REQUEST_CHOICES = Choices(
        (DEFAULT_REQUEST, DEFAULT_REQUEST),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    )

    friend_request_id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(
        USER_MODEL, on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        USER_MODEL, on_delete=models.CASCADE, related_name="receiver"
    )
    status = models.CharField(
        choices=REQUEST_CHOICES, default=DEFAULT_REQUEST, max_length=10
    )
    is_active = models.BooleanField(blank=False, null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("sender", "receiver")

    def __str__(self):
        return f"{self.sender} -> {self.receiver} [{self.status}]"
