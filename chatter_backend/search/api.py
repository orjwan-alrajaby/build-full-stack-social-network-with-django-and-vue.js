from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from post.models import Post
from post.serializers import PostSerializer

from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def search_users_and_posts_list(request, query):  
  users = User.objects.filter(name__icontains=query)
  posts = Post.objects.filter(body__icontains=query).order_by('-created_at')
  
  posts_serializer = PostSerializer(posts, many=True)
  users_serializer = UserSerializer(users, many=True)

  return JsonResponse({'users': users_serializer.data, 'posts': posts_serializer.data}, safe=False)
