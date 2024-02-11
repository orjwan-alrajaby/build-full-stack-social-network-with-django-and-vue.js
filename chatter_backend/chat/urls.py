from django.urls import path
from . import api

urlpatterns = [
    path('conversations/', api.get_conversation_list, name='get_conversation_list'),
    path('conversations/<uuid:conversation_id>/',
         api.get_single_conversation, name="get_single_conversation"),
    path('conversations/<uuid:conversation_id>/send/',
         api.send_message_in_conversation, name="send_message_in_conversation")
]
