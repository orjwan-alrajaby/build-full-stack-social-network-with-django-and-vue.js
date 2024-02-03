from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm
from .models import User, FriendshipRequest


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
      'status': status.HTTP_201_CREATED
    })
  else:    
    if len(form.errors.keys()) > 0:
      return JsonResponse({
        'message': "Bad request. User data is not valid.",
        'status': status.HTTP_400_BAD_REQUEST,
        'errors': form.errors
      })
    return  JsonResponse({'message':'Unexpected error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_friend(request, id):
  
  user = User.objects.get(pk=id)
  
  friendship_request = FriendshipRequest(created_for=user, created_by=request.user)

  return JsonResponse({'message': 'Friend request has been sent!'}, status=status.HTTP_201_CREATED)
