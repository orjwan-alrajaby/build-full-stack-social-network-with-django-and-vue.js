from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Post, Like
from .serializers import PostSerializer
from .forms import PostForm

from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def get_post_list(request):
  users_ids = [request.user.id]
  
  for user in request.user.friends.all():
    users_ids.append(user.id)
  
  posts = Post.objects.filter(created_by_id__in=list(users_ids)).order_by('-created_at')
  
  serializer = PostSerializer(posts, many=True, context={'request': request})
  
  return JsonResponse({'data': serializer.data})


# code above explanation

# In Django ORM, the double underscores (__) are used to traverse relationships between models and access related fields. Here's what each part of created_by_id__in means:

# created_by_id: This assumes that Post model has a field named created_by_id that stores the ID of the user who created the post. This is usually a ForeignKey field linking to the User model or whatever model represents users in your application.

# __in: This is a lookup that checks if the value of the field (created_by_id) is in a given list of values.

# list(users_ids): This converts the list of user IDs (users_ids) into a Python list. users_ids contains the IDs of the current user and all their friends.

# So, created_by_id__in=list(users_ids) translates to "retrieve posts where the created_by_id is in the list of IDs of the current user and their friends".

# In other words, this part of the query ensures that the posts returned are authored by either the current user or any of their friends, as specified in users_ids. This is an efficient way to filter posts based on the authorship of the posts and the relationships between users.

#=================================================
#==================================================
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
  post_serializer = PostSerializer(
      posts, many=True, context={'request': request})
  user_serializer = UserSerializer(user, context={'request': request})

  return JsonResponse({'author': user_serializer.data, 'posts': post_serializer.data}, safe=False)


@api_view(['POST'])
def create_like_for_post(request, id):
  
  post = Post.objects.get(pk=id)
  like_exists = post.likes.filter(
      created_by=request.user).exists()

  if not like_exists: 
    like = Like.objects.create(created_by=request.user)
    post.likes.add(like)
    post.likes_count = post.likes_count + 1

    post.save()

    return JsonResponse({'message': 'Post liked successfully!'}, status=status.HTTP_201_CREATED)
  else:
    # Delete the existing like record
    existing_like = post.likes.get(created_by=request.user)
    existing_like.delete()

    # Decrement the likes count
    post.likes_count = post.likes_count - 1
    post.save()
    return JsonResponse({'message': 'Post unliked successfully!'}, status=status.HTTP_204_NO_CONTENT)
