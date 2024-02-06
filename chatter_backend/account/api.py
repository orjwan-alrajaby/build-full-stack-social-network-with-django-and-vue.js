from django.http import JsonResponse
from rest_framework import status as response_status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(['GET'])
def get_me(request):
  return JsonResponse({
    'id': request.user.id,
    'name': request.user.name,
    'email': request.user.email,
  })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
  data = request.data
  
  form = SignupForm({
    'email': data.get('email'),
    'name': data.get('name'),
    'password1': data.get('password1'),
    'password2': data.get('password2'),
  })
  
  if form.is_valid():
    form.save()
    
    # send verification email sometime.
    
    return JsonResponse({
      'message': 'user created successfully.',
      'status': response_status.HTTP_201_CREATED
    })
  else:    
    if len(form.errors.keys()) > 0:
      return JsonResponse({
        'message': "Bad request. User data is not valid.",
        'status': response_status.HTTP_400_BAD_REQUEST,
        'errors': form.errors
      })
    return  JsonResponse({'message':'Unexpected error.'}, status=response_status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_friend(request, id):
  
  user = User.objects.get(pk=id)
  
  friendship_request = FriendshipRequest.objects.create(created_for=user, created_by=request.user)

  return JsonResponse({'message': 'Friend request has been sent!'}, status=response_status.HTTP_201_CREATED)


@api_view(['GET'])
def get_friends_and_requests(request, id):
  user = User.objects.get(pk=id)
  received_requests = []
  sent_requests = []
  
  # get friend requests sent to the currently logged in user
  if user == request.user:
    received_requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
    sent_requests = FriendshipRequest.objects.filter(
        created_by=request.user, status=FriendshipRequest.SENT)
    
  friends = user.friends.all()
  user_serializer = UserSerializer(user)
  friends_serializer = UserSerializer(
      friends, many=True, context={'request': request})
  received_requests_serializer = FriendshipRequestSerializer(
      received_requests, many=True)
  sent_requests_serializer = FriendshipRequestSerializer(
      sent_requests, many=True)
  
  return JsonResponse({
     'user': user_serializer.data,
     'received_requests': received_requests_serializer.data,
     'sent_requests': sent_requests_serializer.data,
     'friends': friends_serializer.data,
  }, safe=False, status=response_status.HTTP_200_OK)
  
  
@api_view(['POST'])
def respond_to_friend_request(request, status, sender_id):
  
  sender_user = User.objects.get(pk=sender_id)
  
  friendship_request = FriendshipRequest.objects.filter(
      created_for=request.user).get(created_by=sender_user)
  friendship_request.status = status;
  friendship_request.save();
  
  if status == FriendshipRequest.ACCEPTED:
    receiver_user = User.objects.get(pk=request.user.id)

    receiver_user.friends.add(sender_user)
    receiver_user.friends_count = receiver_user.friends_count + 1
    receiver_user.save();
    
    sender_user.friends.add(request.user) 
    sender_user.friends_count = sender_user.friends_count + 1
    sender_user.save();
    
  return JsonResponse({
      'message': 'Friend request has been {frnd_req_status} successfully!'.format(frnd_req_status=status)
  }, safe=False, status=response_status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_friend_request(request, pk):

  user = User.objects.get(pk=pk)
  friendship_request = FriendshipRequest.objects.get(
      created_for=user, created_by=request.user)
  
  friendship_request_cancelled = friendship_request.delete()

  return JsonResponse({'message': 'Friend request has been cancelled successfully!', 'result': friendship_request_cancelled}, status=response_status.HTTP_200_OK)
