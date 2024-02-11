from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer


@api_view(['GET'])
def get_conversation_list(request):
    conversations = Conversation.objects.filter(
        users__in=list([request.user])).order_by('-created_at')
    serializer = ConversationSerializer(conversations, many=True)

    return JsonResponse({
        'message': 'Fetched conversations successfully!',
        'conversations': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_single_conversation(request, conversation_id):
    conversation = Conversation.objects.filter(
        users__in=list([request.user])).get(pk=conversation_id)
    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse({
        'message': 'Fetched conversation successfully!',
        'conversation': serializer.data
    }, safe=False, status=status.HTTP_200_OK)
