from django.urls import path
from . import api

urlpatterns = [
    path('conversations/', api.get_conversation_list, name='get_conversation_list'),
]
