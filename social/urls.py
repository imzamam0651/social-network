from django.urls import include
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"friendrequests", views.FriendRequestViewset)


urlpatterns = [
    url(r"^v1/", include(router.urls)),
    url("v1/user_search", views.UserSearchAPIView.as_view()),
    url("v1/signup", views.SignupAPIView.as_view()),
    url("v1/login", views.LoginAPIView.as_view()),
    url("v1/logout", views.LogoutAPIView.as_view()),
]
