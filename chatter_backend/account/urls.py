from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path("me/", api.get_me, name='get-me'),
    path("signup/", api.signup, name='signup'),
    path("friends/add/<uuid:id>/", api.add_friend, name='add-friend'),
    path("login/", TokenObtainPairView.as_view(), name="obtain-token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh-token"),
]
