from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer
from .forms import PostForm, CommentForm

from account.models import User
from account.serializers import UserSerializer

from django.core.exceptions import ObjectDoesNotExist

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
  user = User.objects.get(pk=request.user.id)
  
  if form.is_valid():
    post = form.save(commit=False)
    post.created_by = request.user
    post.save()
    
    user.posts_count = user.posts_count + 1
    user.save()
  
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

    
@api_view(['POST'])
def create_comment_on_post(request, id):
  form = CommentForm(request.data)
  post = Post.objects.get(pk=id)

  if form.is_valid():
    comment = form.save(commit=False)
    comment.created_by = request.user
    comment.save()
    
    
    post.comments_count = post.comments_count + 1
    post.comments.add(comment)
    
    post.save();
    
    serializer = CommentSerializer(comment)
    return JsonResponse({'comment': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

  return JsonResponse({
    'message': "Bad request. Post data is not valid.",
    'status': status.HTTP_400_BAD_REQUEST,
    'errors': form.errors
  })


@api_view(['GET'])
def get_post_comments_list(request, id):
  post = Post.objects.get(pk=id)
  comments = post.comments.all().order_by('-created_at');
  
  serializer = CommentSerializer(comments, many=True, context={'request': request})

  return JsonResponse({'comments': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_like_for_comment(request, post_id, comment_id):
  comment = Comment.objects.get(pk=comment_id, post__pk=post_id)
  like_exists = comment.likes.filter(
      created_by=request.user).exists()

  if not like_exists: 
    like = Like.objects.create(created_by=request.user)
    comment.likes.add(like)
    comment.likes_count = comment.likes_count + 1

    comment.save()

    return JsonResponse({'message': 'Comment liked successfully!'}, status=status.HTTP_201_CREATED)
  else:
    # Delete the existing like record
    existing_like = comment.likes.get(created_by=request.user)
    existing_like.delete()

    # Decrement the likes count
    comment.likes_count = comment.likes_count - 1
    comment.save()
    return JsonResponse({'message': 'Comment unliked successfully!'}, status=status.HTTP_204_NO_CONTENT)
  
  
@api_view(['DELETE'])
def delete_comment_on_post(request, post_id, comment_id):
  
  post = Post.objects.get(pk=post_id)
  comment_exists = post.comments.filter(
      id=comment_id, created_by=request.user).exists()
  
  if comment_exists:
    # Delete the existing comment record
    comment = post.comments.get(id=comment_id, created_by=request.user)
    
    comment.delete()

    # Decrement the comments count
    post.comments_count = post.comments_count - 1
    post.save()
        
    return JsonResponse({'message': 'Comment deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
  else:
    return JsonResponse({'message': 'Comment already does not exist!'}, status=status.HTTP_409_CONFLICT)


@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.delete()
        user = User.objects.get(pk=request.user.id)
        user.posts_count = user.posts_count - 1
        user.save()
        
        return JsonResponse({'message': 'Post deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Post not found!'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_post_details(request, id):
    try:
        post = Post.objects.get(pk=id)
        post_serializer = PostSerializer(post)
        return JsonResponse({'message': 'Post fetched successfully!', 'post': post_serializer.data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Post not found!'}, status=status.HTTP_404_NOT_FOUND)