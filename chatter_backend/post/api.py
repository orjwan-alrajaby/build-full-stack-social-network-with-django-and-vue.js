from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Post
from .serializers import PostSerializer
from .forms import PostForm

from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def get_post_list(request):
  posts = Post.objects.all().order_by('-created_at')
  serializer = PostSerializer(posts, many=True)
  
  
  return JsonResponse({'data': serializer.data})


@api_view(['POST'])
def create_post(request):
  form = PostForm(request.data)
  
  if form.is_valid():
    post = form.save(commit=False)
    post.created_by = request.user
    post.save()
  
    serializer = PostSerializer(post)
    return JsonResponse({'data': serializer.data}, safe=False)
  else:
    return JsonResponse({
      'message': "Bad request. Post data is not valid.",
      'status': status.HTTP_400_BAD_REQUEST,
          'errors': form.errors
      })

@api_view(['GET'])
def get_profile_post_list(request, id):
  # we have no field called "created_by_id" but we do have an _id field on "created_by"
  posts = Post.objects.filter(created_by_id=id).order_by('-created_at')
  user = User.objects.get(pk=id)
  post_serializer = PostSerializer(posts, many=True)
  user_serializer = UserSerializer(user)

  return JsonResponse({'author': user_serializer.data, 'posts': post_serializer.data}, safe=False)
