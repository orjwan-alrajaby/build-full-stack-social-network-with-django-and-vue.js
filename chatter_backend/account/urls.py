from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path("me/", api.get_me, name='get-me'),
    path("signup/", api.signup, name='signup'),
    path("friends/<uuid:id>/",
         api.get_friends_and_requests, name='get-friends-and-requests'),
    path("friends/<uuid:id>/add/", api.add_friend, name='add-friend'),
    path("friends/request/<uuid:pk>/delete/",
         api.delete_friend_request, name='delete-friend-request'),
    path("friends/request/<uuid:sender_id>/<str:status>/",
         api.respond_to_friend_request, name='respond-to-friend-request'),
    path("login/", TokenObtainPairView.as_view(), name="obtain-token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh-token"),
]
