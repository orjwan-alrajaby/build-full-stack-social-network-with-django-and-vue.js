from .models import Post, Comment
from rest_framework import serializers
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
  created_by = UserSerializer(read_only=True)
  is_liked = serializers.SerializerMethodField()
  has_commented = serializers.SerializerMethodField()
  class Meta:
    model = Post
    fields = ('id', 'body', 'created_by', 'created_at_formatted',
              'likes_count', 'is_liked', 'has_commented')

  def get_is_liked(self, obj):
   request = self.context.get('request')
   if request and request.user.is_authenticated:
        return obj.is_liked_by_user(request.user)
   return False
 
  def get_has_commented(self, obj):
    request = self.context.get('request')
    if request and request.user.is_authenticated:
       return obj.comments.filter(created_by=request.user).exists()
    return False


class CommentSerializer(serializers.ModelSerializer):
  created_by = UserSerializer(read_only=True)
  
  class Meta:
    model = Comment
    fields = ('id', 'body', 'created_by', 'created_at_formatted',)
    
class PostDetailSerializer(serializers.ModelSerializer):
  created_by = UserSerializer(read_only=True)
  comments = CommentSerializer(many=True, read_only=True)
  has_commented = serializers.SerializerMethodField()
  class Meta:
    model = Post
    fields = ('id', 'body', 'created_by', 'created_at_formatted',
              'likes_count', 'is_liked', 'has_commented',)

  def get_is_liked(self, obj):
   request = self.context.get('request')
   if request and request.user.is_authenticated:
       return obj.is_liked_by_user(request.user)
   return False

  def get_has_commented(self, obj):
    request = self.context.get('request')
    if request and request.user.is_authenticated:
       return obj.comments.filter(created_by=request.user).exists()
    return False