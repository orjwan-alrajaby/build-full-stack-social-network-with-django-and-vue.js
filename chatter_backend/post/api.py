from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Post
from .serializers import PostSerializer
from .forms import PostForm

@api_view(['GET'])
def get_post_list(request):
  posts = Post.objects.all()
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
