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
    

@api_view(['POST'])
def send_message_in_conversation(request, conversation_id):
    conversation = Conversation.objects.filter(
        users__in=list([request.user])).get(pk=conversation_id)
    
    message = None
        
    for user in conversation.users.all():
        if user != request.user:
            sent_to = user
            
            message = ConversationMessage.objects.create(
                conversation=conversation,
                body=request.data.get('body'),
                created_by=request.user,
                sent_to=sent_to
            )
            
    serializer = ConversationMessageSerializer(message)

    return JsonResponse({
        'message': 'Sent message {} successfully!'.format(request.data.get('body')),
        'conversation_message': serializer.data
    }, safe=False, status=status.HTTP_201_CREATED)
